# Counting pattern
count = dict()
print('Enter a line of text: ')
line = input('')
if line <= '': line = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    count[word] = count.get(word, 0) + 1
print('Counts', count)



# Definite Loops and Dictionaries
counts = { 'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])



# Retrieving lists of Keys and Values
jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
print(f"{list(jjj)}\n{jjj.keys()}\n{jjj.items()}")



# Bonus: Two Iteration Variables!






# Counting words
dic = dict()
hand = open('mbox.txt')
kay = None
max_kay = None
max_value = None
for line in hand:
    line = line.rstrip().split()
    for word in line:
        i = line.index(word)
        word = line[i]
        kay = word.strip('()".,')
        dic[kay] = dic.get(kay, 0) + 1

for kay in dic:
    max_value = max(dic.values())
    if max_value == dic[kay]:
        max_kay = kay

print(f'{max_kay}: {max_value}')