import os
import requests
from io import StringIO
import csv
from api_config import APIConfig
from itertools import product

def fetch_data(endpoint, parameters=None):
    if parameters is None:
        parameters = {}
    url = endpoint.url.format(**{**endpoint.parameters, **parameters}, API_TOKEN=APIConfig.API_TOKEN)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

def process_data(data, parameters=None):
    csv_data = csv.reader(StringIO(data))
    rows = list(csv_data)
    
    if parameters:
        for param, value in parameters.items():
            for row in rows[1:]:
                row.append(value)
            rows[0].append(param)
    
    total_rows = len(rows)
    total_columns = len(rows[0]) if total_rows > 0 else 0

    data_size = len(data.encode('utf-8'))
    size_unit = 'MB' if data_size >= 1024 * 1024 else 'KB'
    size_value = round(data_size / (1024 * 1024), 2) if size_unit == 'MB' else round(data_size / 1024, 2)

    print(f"Total rows: {total_rows}")
    print(f"Total columns: {total_columns}")
    print(f"Data size: {size_value} {size_unit}")

    return rows

def save_data(rows, parameters):
    data_directory = "data"
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    file_name = "_".join(f"{key}_{value}" for key, value in parameters.items()) + ".csv"
    file_path = os.path.join(data_directory, file_name)
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Data saved to {file_path}")

def get_parameter_combinations(endpoint):
    parameter_combinations = []
    list_parameters = {}
    for param, value in endpoint.parameters.items():
        if isinstance(value, list):
            list_parameters[param] = value
        else:
            list_parameters[param] = [value]

    keys, values = zip(*list_parameters.items())
    for combo in product(*values):
        parameter_combinations.append(dict(zip(keys, combo)))

    return parameter_combinations

def main():
    for endpoint in [APIConfig.MATCHUPS, APIConfig.MATCHUPS_ALL_PAIRINGS, APIConfig.OUTRIGHTS]:
        parameter_combinations = get_parameter_combinations(endpoint)
        for parameters in parameter_combinations:
            data = fetch_data(endpoint, parameters)
            if data:
                rows = process_data(data, parameters)
                save_data(rows, parameters)

if __name__ == "__main__":
    main()