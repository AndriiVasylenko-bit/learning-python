fhand = open('mbox.text')
print(fhand)

# The newline Character
stuff = 'Hello\nWorld!' # 'Hello\nWorld!'
print(stuff)
stuff = 'X\nY'
print(stuff)
len(stuff)

#Reading Files in Python
xfile = open('mbox.text')
for cheese in xfile:
    print(cheese)