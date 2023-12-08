import re

data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)



# The Double Split Pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


# The Regex Version
y = re.findall('@([^ ]*)', data)
# @ Look through the string until you find an at sign.
# () Extract the non-blank character.
# [] Match non-blank character (not spase).
# * Match many of them (run until he finds a spase).
print(y[0])



# Even Cooler Regex Version
y = re.findall('^From .*@([^ ]*)', data)
# ^ Starting at the beginning of the line, look for the string 'From'
print(y[0])



#Spam confidence
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))



# Escape Character
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
# \$ A Real dollar sign.
# [0-9.] A digit or period.
# At least one more.
print(y[0])
