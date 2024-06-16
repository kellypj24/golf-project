import os
import requests
from io import StringIO
import csv

API_TOKEN = os.environ.get("DATAGOLF_API_TOKEN")
API_URL = f"https://feeds.datagolf.com/betting-tools/matchups?tour=pga&market=tournament_matchups&odds_format=american&file_format=csv&key={API_TOKEN}"

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
    
    print(f"Total rows: {total_rows}")
    print(f"Total columns: {total_columns}")
    print(f"Data size: {size_value} {size_unit}")
else:
    print(f"Request failed with status code: {response.status_code}")