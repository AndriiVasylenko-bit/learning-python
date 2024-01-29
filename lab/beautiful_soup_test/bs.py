from bs4 import BeautifulSoup

with open('beautiful_soup_test/index.html') as file:
    lst = file.readlines()

html = ''
for element in lst:
    html += element

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
count = 0
for tag in tags:
    href = tag.get('href', None)
    count += 1
    print(count, href)