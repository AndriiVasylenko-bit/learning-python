import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = "http://py4e-data.dr-chuck.net/comments_1848643.json"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url, context=ctx).read()

line = json.loads(data)
line = line['comments']
count = 0

for item in line:
    count += item['count']
print('Sum: ', count)