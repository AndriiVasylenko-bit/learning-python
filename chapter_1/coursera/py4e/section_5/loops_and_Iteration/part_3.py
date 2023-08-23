# Looping Through a Set/Петля через набор

print('Brfore')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')

# What is the largest Number?
numbers = [3, 41, 12, 9, 74, 15]
max = numbers[1]
for number in numbers:
    if max < number:
        max = number
print(max)