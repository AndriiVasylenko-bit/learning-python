# Best Friends: Strings and Lists

abc = 'With three words'
stuff = abc.split()
print(f"{stuff}\n{len(stuff)}\n{stuff[0]}\n{stuff}")

for w in stuff: print(w)

line = 'A lot                        of spaces'
print(line.split())

line = 'first;second;third'
print(f"{line.split()}\n{len(line.split())}")

print(f"{line.split(';')}\n{len(line.split(';'))}")