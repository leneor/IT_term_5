import numpy as np
import math

# Начальные данные
x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
y = np.array([0.000, 0.033, 0.067, 0.100, 0.133, 0.166, 0.199, 0.231, 0.264, 0.296, 0.327])

h = 0.1
x_0 = 0.95
f_11 = 10 ** (-6)


# Считаем полином Лагранжа в точке x_0
def lagranz(x, y, x_0):
    Y = 0
    for j in range(len(y)):
        numerator = 1;
        denominator = 1
        for i in range(len(x)):
            if i == j:
                numerator = numerator
                denominator = denominator
            else:
                numerator = numerator * (x_0 - x[i])
                denominator = denominator * (x[j] - x[i])
        Y = Y + y[j] * numerator / denominator
    return Y


delta = h ** len(x)/ len(x) * f_11
f = lagranz(x, y, x_0)

print('f(0.95) =', f, '; delta =', delta)
