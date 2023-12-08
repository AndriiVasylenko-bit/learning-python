# Repeated Steps.

n = 5 # Переменная итерации.
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff') # "Отрыв"
print(n)



# An Infinite Loop/бесконечный цикл

n = 5
while n > 0 :
    print('Lather/пена')
    print('Rinse/полоскать')
print('Dry off!/А ну, высохни!')



# Another Loop

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')



# Breaking Out of a Loop

while True :
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')



# Finishing an Iteration with Continue

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')