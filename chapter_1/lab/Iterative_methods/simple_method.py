import math

# x1, x2, x3, x4 = 2.75, 2, -1, 1.5
#
# new_x1 = -0.75 * x2 + 1.25 * x3 + 1.5
# new_x2 = -1.5 * x1 + 2.5 * x4 - 1
# new_x3 = 0.5 * x1 + 1.5 * x4 + 2
# new_x4 = -0.25 * x1 + 0.5 * x2 - 0.75 * x3 + 2.75

def upround(v): return math.ceil(v * 100) / 100

print(upround(9.355))
print(round(3.555, 2))

x1, x2, x3 = 0.75, 1.84, -0.47
new_x1 = (0.75 + (0.1 * x2) - (0.05 * x3))
new_x2 = (1.84 + (0.04 * x1) - (0.12 * x3))
new_x3 = (-0.47 + (0.13 * x1) - (0.33 * x2))
# dx1 = x1 - new_x1
# dx2 = x2 - new_x2
# dx3 = x3 - new_x3
# dx4 = x4 - new_x4

print('x1 ', new_x1)
print('x2 ', new_x2)
print('x3 ', new_x3)
# print('x4 ', new_x4)