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



x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+', x)
# \S+@\S+ At least one non-whitespace character (По крайней мере один символ неблокового пространства)
print(y)



# Parentheses are not part of the match - but they tell where to start and stop what string to extract
y = re.findall('^From (\S+@\S+)', x)
print(y)