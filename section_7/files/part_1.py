xfile = open('mbox.txt')
for cheese in xfile:
    cheese = cheese.rstrip()
    print(cheese)

# The newline Character
stuff = 'Hello\nWorld!' # 'Hello\nWorld!'
print(stuff)
stuff = 'X\nY'
print(stuff)
len(stuff)