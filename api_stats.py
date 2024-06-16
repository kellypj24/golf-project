import os
import requests
from io import StringIO
import csv

API_TOKEN = os.environ.get("DATAGOLF_API_TOKEN")
API_URL = f"https://feeds.datagolf.com/betting-tools/matchups?tour=pga&market=tournament_matchups&odds_format=american&file_format=csv&key={API_TOKEN}"

def main():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.text
        
        # Count the total rows and columns
        csv_data = csv.reader(StringIO(data))
        rows = list(csv_data)
        total_rows = len(rows)
        total_columns = len(rows[0]) if total_rows > 0 else 0
        
        # Calculate the size of the data
        data_size = len(data.encode('utf-8'))
        size_unit = 'MB' if data_size >= 1024 * 1024 else 'KB'
        size_value = round(data_size / (1024 * 1024), 2) if size_unit == 'MB' else round(data_size / 1024, 2)
        
        # Print the stats to the console
        print(f"Total rows: {total_rows}")
        print(f"Total columns: {total_columns}")
        print(f"Data size: {size_value} {size_unit}")
        
        # Create the data directory if it doesn't exist
        data_directory = "data"
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)
        
        # Write the data to a CSV file in the data directory
        file_name = "tournament_matchups.csv"
        file_path = os.path.join(data_directory, file_name)
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print(f"Data saved to {file_path}")
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    main()