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
jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
for aaa,bbb in jjj.items():
    print(aaa, bbb)



# Counting words
handle = open('mbox.txt')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)



# Right counting words
handle = open('mbox.txt')

kay = None
dic = dict()
for line in handle:
    line = line.rstrip().split()
    for word in line:
        i = line.index(word)
        word = line[i]
        kay = word.strip('()".,')
        dic[kay] = dic.get(kay, 0) + 1

max_kay = None
max_value = None

for k, v in dic.items():
    if max_kay is None or v > max_value:
        max_kay = k
        max_value = v

print(f'{max_kay}: {max_value}')