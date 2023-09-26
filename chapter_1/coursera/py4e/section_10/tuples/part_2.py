# Sorting Lists of Tuples
d = {'a':10, 'c':22, 'b':1}
print(f"{d.items()}\n"
      f"{sorted(d.items())}")



# Using sorted()


d = {'a':10, 'c':22, 'b':1}
for (k, v) in sorted(d.items()):
    print(k, v)



# Sort by values instead of kay
c = {'a':10, 'c':22, 'b':1}
tmp = list()
for (k, v) in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

# Te top 10 most common words

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        word = word.strip('"():.,—')
        counts[word] = counts.get(word, 0) + 1

lst = list()
for (kay, val) in counts.items():
    newtup = (val, kay)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for (val, key) in lst[:10]:
    print(key, val)