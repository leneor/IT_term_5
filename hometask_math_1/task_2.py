import math

import numpy as np


def f(x):
    y = math.sin(100*x)*math.exp(-x**2)*math.cos(2*x)
    return y


a = 0
b = 3
x = np.array([a + (b - a) * i / 100000 for i in range(100000)])
h = x[1] - x[0]

# Средние прямоугольники
F_average = sum(f((x[i - 1] + x[i]) / 2) * h for i in range(len(x)))

# Левые прямоугольники

F_left = sum(f(x[i - 1]) * h for i in range(len(x)))

# Правые прямоугольник

F_right = sum(f(x[i]) * h for i in range(len(x)))

# Трапеции

F_trapezoid = sum(((f(x[i - 1]) + f(x[i])) / 2) * h for i in range(len(x)))

# Симпсон

F_simpson = sum(((f(x[i - 1]) + 4 * f(x[i - 1] / 2 + x[i] / 2) + f(x[i])) / 6) * h for i in range(len(x)))

# 3/8

F_threeeight = sum(
    ((f(x[i - 1]) + 3 * f(2 * x[i - 1] / 3 + x[i] / 3) + 3 * f(x[i - 1] / 3 + 2 * x[i] / 3) + f(x[i])) / 8) * h for i in
    range(len(x)))

print(F_average, '\n', F_left, '\n', F_right, '\n', F_trapezoid, '\n', F_simpson, '\n', F_threeeight)
