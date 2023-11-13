import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1848640.html')
soup = BeautifulSoup(html, 'html.parser')

amount = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    amount += int(tag.contents[0])
print('Sum', amount)