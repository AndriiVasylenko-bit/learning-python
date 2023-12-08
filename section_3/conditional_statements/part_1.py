# example 1
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

# example 2
x = 5
if x == 5 : print('Equals 5')
if x > 4 : print('Greater than 4')
if x >= 5 : print('Greater than or Equals 5')
if x < 6 : print('Less then 6')
if x <= 5 : print('Less than or Equals 5')
if x != 6 : print('Not equal 6')

# example 3
x = 5
print ('Before 5')
if x == 5 :
    print('Is/вот 5')
    print('Is Still/все еще 5')
    print('Third/третий 5')
print('Afterwards/после 5')
print('Before 6')
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('third 6')
print('Afterwards 6')

# example 4
x = 5
if x > 2 :
    print('Bigger than/Больше чем 2')
    print('Still bigger/Все еще больше')
print('Done with/Закончили с 2')

for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

# examle 5
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than/меньше 100')
    print('All done')

# example 6. Two-way Decisions whith eles:
# Двусторонние решения с помощью elxe:
x = 4

if x > 2 :
    print('Bigger')
else :
    print('Smaller')

print('All done')
