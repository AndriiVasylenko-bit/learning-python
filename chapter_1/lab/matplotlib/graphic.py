import matplotlib.pyplot as plt
import numpy as np

# Обчислення значень ч в діапазоні
x = np.linspace(-10,10,400) # вибриаємо діапазон значень х

# Обчислення значень y
y = 4 * x**3 / (x**3 - 1)

# Побудов графіка
plt.figure(figsize=(8,6))
plt.plot(x, y, label=r'$y = \frac{4x^3}{x^3 - 1}$')
plt.title('Графік функції')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0, color='red', linestyle='--', label='y=0') # лінія для y=0
plt.axvline(x=0, color='blue', linestyle='--', label='x=0')
plt.legend()
plt.grid(True)
plt.show()