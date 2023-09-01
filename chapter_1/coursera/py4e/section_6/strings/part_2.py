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
    