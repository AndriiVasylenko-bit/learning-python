# Slicing Strings
sub = 'Monty Python'
print(sub[0:4])
print(sub[6:7])
print(sub[6:20])


sub = 'Monty Python'
print(sub[:2])
print(sub[8:])
print(sub[:])



# String Concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)



# Using in as a logical Operator
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit :
    print('Found it!/нашел его!')



# String Comparison/сравнение
word = input('Enter word: ')
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')



# String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

stuff = 'Hello World'
print(type(stuff))
print(dir(stuff))
print(stuff.lower())

# String Library
str = 'Hello World'


print(str.capitalize())

width = 100
fillchar = '_'
c_str = str.center(width, fillchar)
print(c_str)

print(str.endswith('jockey'))
print(str.endswith('World'))
print(str.endswith('jockey', 2))
print(str.endswith('Hello', 0,5))

print(str.find('or'))
print(str.find('l', 4))
print(str.find('l', 1,2))
print('or' in str)

print(str.lstrip('H'))

print(str.replace('World', 'Python'))
print(str.replace('W', 'w',1))

print(str.lower())
print(str.rstrip('dl'))

print(str.strip('Hd'))

print(str.upper())




# Searching a String/Поиск по строке
fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)



# Making everything UPPER CASE
greet = 'Hello Bob'
nnn = greet.upper()
print(greet)

www = greet.lower()
print(www)



# Search and Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

nstr = greet.replace('o', 'O')
print(nstr)



# Stripping Whitespace/Зачистка пробела
greet = '        Hello Bob    '
print(greet.lstrip())
print(greet.rstrip())
print((greet.strip()))



# Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))



# Parsing and Extracting/Разбор и извлечение
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# Two Kinds of Strings
x = '你好'
print(type(x))
x = u'你好'
print(type(x))