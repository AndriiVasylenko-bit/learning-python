import re
# [0-9]+ One ro more digits
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[AEIOU]+', x) # One or more uppercase letters
print(y)



# Warning: Greedy Batching
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
# ^F First character in the match is an F
# .+ One or more characters
# : Last character in the match is a:
y = re.findall('^F.+?:', x)
print(y)
# .+? One or more characters but not greedy
