import math
import numpy as np


def f(x):
    y = x ** 2 + math.tan(x) ** 2 - 1
    return y


# Решить систему (1) x^2+y^2=1; y=tg(x)

a = -1
b = 1

# Корни симметричны, поэтому достаточно найти корень на отрезке [0;1]

a = 0


# Локализация корней
def find_roots():
    a_root = np.array([])
    point = [a + i * (b - a) / 10000 for i in range(10000)]
    for i in range(0, 9999):
        if (f(point[i]) * f(point[i + 1]) < 0):
            a_root = np.append(a_root, point[i])
    return a_root


# Ищем отрезки с корнями.
root_a = find_roots()
root_b = root_a + (b - a) / 1000


# Используем метод дихотомии для поиска точного значения корня.
def precise_root(a, b):
    for i in range(100):
        c = (a + b) / 2
        if (f(c) * f(b) < 0):
            a = c
            b = b
        else:
            a = a
            b = c

        if round(a - b, 15) == 0:
            return b


root_x_1 = 0

root_x_1 = precise_root(root_a[0], root_b[0])
root_y_1 = math.tan(root_x_1)

# Ищем отрицательный корень
a = -1
b = 0

root_a = find_roots()
root_b = root_a + (b - a) / 1000
root_x_2 = 0

root_x_2 = precise_root(root_a[0], root_b[0])
root_y_2 = math.tan(root_x_2)

# Выводим корни
print(round(root_x_1,6), round(root_y_1,6), '\n', round(root_x_2,6), round(root_y_2,6))


