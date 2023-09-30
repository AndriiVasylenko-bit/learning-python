import re

# re.search()
# re.findall()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# ^ - Соответствовать началу строки

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)

# * - во многих случаях
# . - Соответствовать любому символу