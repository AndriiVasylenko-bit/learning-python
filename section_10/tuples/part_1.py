# Tuples are like lists
x = ('Gleen', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(max(y))

for iter in y:
    print(iter)

# But... Tuples are "immutable"
x = [9, 8, 7]
x[2] = 6
print(x)

y = 'ABC'
try: y[2] = 'D'
except: print("TypeError: 'str' object does not support item assignment")

z = (5, 4, 3)
try: z[2] = 0
except: print("TypeError: 'tuple' object does not support item assignment")



# Things not to do with tuple
x = (3, 2, 1)
try: print(x.sort())
except: print("AttributeError: 'tuple' object has no attribute 'sort'")
try: print(x.apped(5))
except: print("AttributeError: 'tuple' object has no attribute 'apped'")
try: print(x.reverse())
except: print("AttributeError: 'tuple' object has no attribute 'reverse'")



# A Tale of Two Sequences
l = list()
print(dir(l))
t = tuple()
print(dir(t))



# Tuples and Assignment
(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)



# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)



# Tuples are Comparable
print(f"{(0, 1, 2) < (5, 1, 2)}\n"
      f"{(0, 1, 2000000) < (0, 3, 4)}"
      f"{('Josep', 'Sally') < ('Josep', 'Sam')}\n"
      f"{('Josep', 'Sally') > ('Adams', 'Sam')}")