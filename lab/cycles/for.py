# for i in range(2):
#     for j in range(2):
#         for x in range(2):
#             print(i, j, x)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x and y) <= (not(z)) and (x <= y)) or w):
                    print(x, y, z, w)
