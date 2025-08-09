import requests
import json

API_KEY = 'JwnFKtfU5nIXFIpwDx45SjOgtA0flZ8S1Kw2o4Wc'

url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {
    'sol': 1000,
    'api_key': API_KEY
}

response = requests.get(url, params=params)
data = response.json()

with open('mars_photos.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Saved response to mars_photos.json")
