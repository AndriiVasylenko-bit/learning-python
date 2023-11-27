import urllib.request, urllib.parse, urllib.error
import json

# Ваш ключ geocoding api google.
api_key = ''
serviceurl = f'https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&'

while True:
    # Адреса міста.
    address = input('Enter location: ')
    # Якщо довжина адреси менше 1 почати цикл заново.
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

    if not js or 'status' not in js or js['status'] != 'Ok':
        print(' ==== Failure To Retrieve ==== ')
        print(data)
        continue

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)
