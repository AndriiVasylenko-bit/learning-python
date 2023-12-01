import urllib.request, urllib.parse, urllib.error
import twurl
import json

# api twitter friend list json
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    # вести існуючий акаунт твіттер
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    # Запрошуємо 5 перших друзів та кодуємо url.
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})

    print('Retrieving', url)
    # Встановлюємо з'єднання з апі.
    connection = urllib.request.urlopen(url)
    # Читаємо та декодуємо дані (розв'язуємо задачу з utf8).
    data = connection.read().decode()
    # Зберігаємо заголовки в словнику.
    headers = dict(connection.getheaders())
    # Виводимо решту данних.
    print('Remaining', headers['x-rate-limit-remaining'])
    # Обробляємо дані за допомогою json.loads.
    js = json.loads(data)
    # Створюємо дамп, з відступом 4.
    print(json.dumps(js, indent=4))

    # Виводимо користувачів.
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50])
