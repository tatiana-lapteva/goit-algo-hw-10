"""
Завдання 2. Обчислення визначеного інтеграла.

Обчислення значення інтеграла функції методом Монте-Карло.
"""


import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi


def is_inside(x, y):
    return y <= f(x)

def monte_carlo_simulation(a, b, num_experiments):
    inside_points = 0
    for _ in range(num_experiments):
        x_rand = random.uniform(a, b)
        y_rand = random.uniform(0, f(b))
        if is_inside(x_rand, y_rand):
            inside_points += 1
    integral = (inside_points / num_experiments) * (b - a) * f(b)
    return integral


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(a, b, 400)
y = f(x)

num_experiments = 10000
integral = monte_carlo_simulation(a, b, num_experiments)
print(f"Середнє значення інтегралу за {num_experiments} експериментів методом Монте-Карло: {integral}")

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Перевірка - Інтеграл: ", result)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


