import json

with open('GeoJSON.json', 'r') as file:
    lines = file.readlines()

data = ''
for line in lines:
    data += line.strip()

js = json.loads(data)
lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
