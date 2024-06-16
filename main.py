import os
import requests

API_TOKEN = os.environ.get("DATAGOLF_API_TOKEN")
API_URL = f"https://feeds.datagolf.com/betting-tools/matchups?tour=pga&market=tournament_matchups&odds_format=american&file_format=csv&key={API_TOKEN}"

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.text
    print("Connection successful. Sample data:")
    print(data[:1000])  # Print the first 1000 characters of the response
else:
    print(f"Request failed with status code: {response.status_code}")