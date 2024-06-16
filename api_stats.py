import os
import requests
from io import StringIO
import csv
from api_config import APIConfig

def fetch_data(endpoint):
    url = endpoint.url.format(**endpoint.parameters, API_TOKEN=APIConfig.API_TOKEN)
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        return data
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

def process_data(data):
    csv_data = csv.reader(StringIO(data))
    rows = list(csv_data)
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

    file_name = f"{parameters['tour']}_{parameters.get('market', 'all_pairings')}_{parameters['odds_format']}.{parameters['file_format']}"
    file_path = os.path.join(data_directory, file_name)
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Data saved to {file_path}")

def main():
    # Fetch data using the matchups endpoint
    matchups_data = fetch_data(APIConfig.MATCHUPS)
    if matchups_data:
        matchups_rows = process_data(matchups_data)
        save_data(matchups_rows, APIConfig.MATCHUPS.parameters)
    
    # Fetch data using the matchups all pairings endpoint
    all_pairings_data = fetch_data(APIConfig.MATCHUPS_ALL_PAIRINGS)
    if all_pairings_data:
        all_pairings_rows = process_data(all_pairings_data)
        save_data(all_pairings_rows, APIConfig.MATCHUPS_ALL_PAIRINGS.parameters)

if __name__ == "__main__":
    main()