from bs4 import BeautifulSoup
from urllib.request import urlopen

document = urlopen('http://www.dr-chuck.com')

html = document.read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
count = 0
for tag in tags:
    href = tag.get('href', None)
    count += 1
    print(count, href)



