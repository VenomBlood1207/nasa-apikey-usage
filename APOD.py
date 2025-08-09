import requests
import json

API_KEY = 'JwnFKtfU5nIXFIpwDx45SjOgtA0flZ8S1Kw2o4Wc'
url = "https://api.nasa.gov/planetary/apod"
params = {
    'api_key': API_KEY,
    'count': 3  # Get 3 random images
}

response = requests.get(url, params=params)
data = response.json()

# Save JSON metadata
with open("apod.json", "w") as f:
    json.dump(data, f, indent=4)

# Download each image
for item in data:
    if item['media_type'] == 'image':
        img_url = item['hdurl']
        filename = img_url.split('/')[-1]
        img_data = requests.get(img_url).content
        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded: {filename}")
