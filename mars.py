import os
import requests
import json
from pathlib import Path
from urllib.parse import urlparse

API_KEY = 'JwnFKtfU5nIXFIpwDx45SjOgtA0flZ8S1Kw2o4Wc'
ROVER_NAME = 'curiosity'
SOL = 1000
MAX_IMAGES = 1

output_dir = Path(f'mars_photos_sol_{SOL}')
output_dir.mkdir(parents=True, exist_ok=True)

url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{ROVER_NAME}/photos"
params = {
    'sol': SOL,
    'api_key': API_KEY
}
print("Fetching photo metadata...")
response = requests.get(url, params=params)
data = response.json()

metadata_file = output_dir / 'metadata.json'
with open(metadata_file, 'w') as f:
    json.dump(data, f, indent=4)
print(f"Metadata saved to {metadata_file}")

photos = data.get('photos', [])
if not photos:
    print("No photos found.")
    exit()

print(f"Downloading up to {MAX_IMAGES} images...")
for i, photo in enumerate(photos[:MAX_IMAGES]):
    img_url = photo['img_src']
    img_name = os.path.basename(urlparse(img_url).path)
    img_path = output_dir / img_name

    img_data = requests.get(img_url).content
    with open(img_path, 'wb') as f:
        f.write(img_data)

    print(f"Saved: {img_path}")

print("Done.")
