print('A B F')
for a in range(2):
    for b in range(2):
        f = not (a and b) or not (b and a)
        f = int(f)
        print(a, b, f)

print('A B F')
for a in range(2):
    for b in range(2):
        f = not (a == b) or not (a) or (a or b)
        f = int(f)
        print(a, b, f)

print('Q P F')
for q in range(2):
    for p in range(2):
        f = q or p or (q)
        f = int(f)
        print(q, p, f)

print('X Y F')
for x in range(2):
    for y in range(2):
        f = not (x) or (y and x)
        f = int(f)
        print(x, y, f)