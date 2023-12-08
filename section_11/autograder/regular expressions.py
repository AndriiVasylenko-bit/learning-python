import re

hand = open('regex_sum_1848638.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1 : continue
    for num in stuff:
        numlist.append(int(num))
print('Numbers:', len(numlist), 'Sum: ', sum(numlist))