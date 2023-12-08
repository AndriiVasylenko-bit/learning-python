# Counting in a Loop

count = 0
print('Before', count)
for thing in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    print(count, thing)
print('After', count)



# Summing in a Loop

total = 0
print('Before', total)
for thing in [9, 41, 12, 3, 74, 15] :
    total = total + thing
    print(total, thing)
print('After', total)



# Finding the Average in a Loop

count = 0
sum = 0
print('Before', sum, count)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, int(sum / count))



# Filtering in a Loop

print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print('Large number', value)
print('After')



# Search Using a Boolean Variable

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
        break
    print(found, value)
print('After', found)



# How to Find the Smallest Value

numbers = [3, 41, 12, 9, 74, 15]
min = numbers[1]
for number in numbers:
    if min > number:
        min = number
print(min)

# OR

smallest = None
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None : smallest = value
    elif value < smallest : smallest = value
    print(smallest, value)
print('After', smallest)