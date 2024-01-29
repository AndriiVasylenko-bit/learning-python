# import random
#
# class TLine:
#     def __init__(self, dimension):
#         self.dimension = dimension
#
# class Line2D(TLine):  # Наслідування класу TLine для прямих на площині
#     def __init__(self, a, b, c):
#         super().__init__(2)  # Площина - двовимірна
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_parallel(self, other):
#         return self.a * other.b == self.b * other.a  # Формула для перевірки паралельності прямих на площині
#
#     def is_perpendicular(self, other):
#         return self.a * other.a + self.b * other.b == 0  # Формула для перевірки перпендикулярності прямих на площині
#
# class Line3D(TLine):  # Наслідування класу TLine для прямих в просторі
#     def __init__(self, a, b, c, d):
#         super().__init__(3)  # Простір - тривимірний
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def is_parallel(self, other):
#         return self.a * other.b == self.b * other.a and self.b * other.c == self.c * other.b and self.a * other.c == self.c * other.a  # Формула для перевірки паралельності прямих в просторі
#
#     def is_perpendicular(self, other):
#         return self.a * other.a + self.b * other.b + self.c * other.c == 0  # Формула для перевірки перпендикулярності прямих в просторі
#
# # Генерація випадкових прямих на площині
# m = 5  # Кількість прямих на площині
# lines_2d = []
# for _ in range(m):
#     a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
#     line = Line2D(a, b, c)
#     lines_2d.append(line)
#
# # Генерація випадкових прямих в просторі
# n = 5  # Кількість прямих в просторі
# lines_3d = []
# for _ in range(n):
#     a, b, c, d = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
#     line = Line3D(a, b, c, d)
#     lines_3d.append(line)
#
# # Пошук прямої у просторі, що перпендикулярна до всіх інших прямих у просторі
# perpendicular_line = None
# for line in lines_3d:
#     is_perpendicular_to_all = all(line.is_perpendicular(other_line) for other_line in lines_3d if other_line != line)
#     if is_perpendicular_to_all:
#         perpendicular_line = line
#         break
#
# if perpendicular_line:
#     print("Пряма у просторі, що є перпендикулярною до всіх інших прямих:")
#     print(perpendicular_line.a, perpendicular_line.b, perpendicular_line.c, perpendicular_line.d)
# else:
#     print("Такої прямої у просторі, що є перпендикулярною до всіх інших, не знайдено.")


import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x + 3)**3 / (x + 1)**2

# Генерація значень x в інтервалі від -10 до 10 з кроком 0.1
x_values = np.arange(-10, 10, 0.1)
# Визначення відповідних значень y
y_values = func(x_values)

# Побудова графіка
plt.plot(x_values, y_values, label='y = (x + 3)^3 / (x + 1)^2')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Графік функції')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
