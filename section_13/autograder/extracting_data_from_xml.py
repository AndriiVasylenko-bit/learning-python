import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = ' http://py4e-data.dr-chuck.net/comments_1848642.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)
comments = tree.findall('.//comment')

count = 0
for comment in comments:
    count += int(comment.find('count').text)
print('Sum:', count)

