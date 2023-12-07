import urllib.request, urllib.parse, urllib.error
import json

with open('api.json', 'r') as file:
    lines = file.readlines()

data = ''
for line in lines:
    data += line.strip()

js = json.loads(data)

# Ваш ключ geocoding api google.
serviceurl = f'https://maps.googleapis.com/maps/api/geocode/json?key={js["api_kay"]}&'

while True:
    # Адреса міста.
    address = input('Enter location: ')
    # Якщо довжина адреси менше 1 припинити програму.
    if len(address) < 1: break

    # URL-адресне кодування.
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    # Відкриваємо посилання та зчитуємо дані.
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    # Якщо дані не вдалося отримати повертаємося на початок циклу.
    if not js or 'status' not in js or js['status'] != 'Ok':
        print(' ==== Failure To Retrieve ==== ')
        print(data)
        continue
# Отримання даних та вивід їх на консоль.
lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
