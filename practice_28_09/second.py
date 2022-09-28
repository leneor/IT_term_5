import numpy as np
import math

# Начальные данные
x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
y = np.array([0.000, 0.033, 0.067, 0.100, 0.133, 0.166, 0.199, 0.231, 0.264, 0.296, 0.327])
x_0 = 0.95
l = len(x)
h = 0.1

f_4 = 0.1
a = y
b = []
d = []
g = []  # Вектор свободных членов в СЛАУ для поиска "с"

# Коэфф. сплайнов a, b, c, d:
at = [1] * (l - 2)  # с = const, так как сетка равномерная
bt = [4] * (l - 2)
ct = [1] * (l - 2)

z = math.floor(x_0 * 10)


# Трехдиагональная прогонка: ( x[i] = alpha[i+1] * x[i+1] + beta[i+1] )
def three_go(a, b, c, g):
    alpha = [-c[0] / b[0]]  # Начальные значения коэффициентов
    beta = [g[0] / b[0]]
    L = len(g)
    result = [0] * L

    # Считаем коэффициенты
    for i in range(1, L):
        alpha.append(-c[i] / (a[i] * alpha[i - 1] + b[i]))
        beta.append((g[i] - a[i] * beta[i - 1]) / (a[i] * alpha[i - 1] + b[i]))

    result[L - 1] = beta[L - 1]

    # Обратная прогонка
    for i in range(L - 1, 0, -1):
        result[i - 1] = alpha[i - 1] * result[i] + beta[i - 1]

    return result


for i in range(1, l - 1):
    g.append(3 * (a[i - 1] - 2 * a[i] + a[i + 1]) / h ** 2)

c = three_go(at, bt, ct, g)  # Трехдиагональная прогонка
c = np.insert(c, [0, len(c)], [0, 0])  # Учет граничных условий

# Находим b и d по формулам
for i in range(1, l):
    b.append((a[i] - a[i - 1]) / h + (2 * c[i] + c[i - 1]) * h / 3)
    d.append((c[i] - c[i - 1]) / (3 * h))

# Вычисляем значение функции в точке
f = a[z] + b[z] * (x_0 - x[z]) + c[z] * (x_0 - x[z]) ** 2 + d[z] * (x_0 - x[z]) ** 3
delta = (f_4 * (x_0 - x[z]) ** 2 * (x_0 - x[z + 1]) ** 2) / (2 * 3 * 4)  # Оценка погрешности
print("f(0.95) = ", f, "; погрешность = ", delta)
