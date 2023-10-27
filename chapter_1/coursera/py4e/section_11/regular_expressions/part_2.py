import re
# [0-9]+ One ro more digits
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[AEIOU]+', x) # One or more uppercase letters
print(y)