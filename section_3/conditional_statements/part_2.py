# example 1. "elif"
x = 2
if x < 2 :
    print('small')
elif x < 10 :
    print ('Medium')
else :
    print('LARGE')

print('All doen')

# example 2 elif
x = 2
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')

print('All doen')

# example 2. "elif"
x = 2
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 40 :
    print('Large/большой')
elif x < 100 :
    print('Huge/огромный')
else :
    print('Ginormous')

print('All doen')



# Which will never print regardless of the value for x?
# Который никогда не будет печататься независимо от значения для х?

if x < 2 :
    print('Below 2')
elif x >= 2 :
    print('Two or more')
else: # never print
    print('Something else/что-то другое')

if x < 2 :
    print('Below 2')
elif x < 20 :
    print('Below 20')
elif x < 10 : # never print
    print('Below 10')
else :
    print('Something else')



# Traceback/отследить
# astr = 'Hello Bob'
# istr = int(astr) # ValueError
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)

# try - попытка, except - исключить
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First/первый', istr)
try:
    astr = '123'
except:
    astr = -1
istr = int(astr)
print('Second', istr)

# Profesional programmer don't use try/excetp.
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print(istr)
except:
    istr = -1

print('Done', istr)



# Raw enter a naumber.
rawstr = input('Enter a naumber: ') # Необработанный.
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print('Nice work')
else:
    print('Not a number')