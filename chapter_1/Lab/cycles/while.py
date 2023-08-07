# Цикл while проверяет истинность некоторого условия, и если условие истинно, то выполняет инструкции цикла.

# Example 1
i = 1
n = 5
# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

# Example 2
i = 5
while i < 15:
    print(i)
    i = i + 2

# Example 3
number = 1
while number < 5:
    print(f'number = {number}')
    number += 1
print('The program is complete')

# Example 4 used else
number1 = 1
while number1 > 5:
     print(f'number = {number1}')
     number1 += 1
else:
    number1 += 1
    print(f'number = {number1}')
print("The program is complete")

# Example 5
# program to calculate the sum of numbers
# until the user enters zero
total = 0
number = int(input('Enter a number: '))
# add numbers until numbers is zero
while number != 0:
    total += number # total = total + number

    # take intrger input agin
    number = int(input('Entar a number. '))
print('total =', total)

counter = 0
while counter < 3:
    # loop ends cecasude of break
    if counter == 1:
        break

    print('Inside loop')
    counter =+ 1
else:
    print('Inside else')