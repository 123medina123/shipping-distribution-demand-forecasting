import requests
import json

def ingest_data():
    # Define the URL of the API
    url = "http://api.example.com/data"

    # Send a GET request to the API
    response = requests.get(url)

    # Check that the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = json.loads(response.text)
        # Do something with the data...
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

if __name__ == "__main__":
    ingest_data()