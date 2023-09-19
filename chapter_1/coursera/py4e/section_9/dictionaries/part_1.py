# What is not a "Collection"?
x = 2
x = 4
print(x)



# Dictionaries
purse = dict() # кошелек
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)



# Comparing/сравнение Lists and Dictionaries
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)



# Dictionary Literals (Counstants)
jjj = {'chuck': 1, 'friend': 42, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)
