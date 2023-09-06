# File Handle as a Sequence
xfile = open('mbox.txt')
for cheese in xfile:
    cheese = cheese.rstrip()
    print(cheese)



# Counting Lines in a File
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)



# Reading the *Whole* File
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:55])



# Searching Through a File
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') : # починається з
        print(line)



# Using in to select lines
fhand = open('mbox.txt')
for line in fhand:
    line =  line.rstrip()
    if not '@collab' in line:
        continue # продовжувати
    print('>', line)



# Prompt for File Name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)


# Bad File Names
fname = input('Enter the file name: ')
try:
    fhand = open()
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'subject lines in', fname)