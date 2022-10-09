import math
import numpy as np

gamma_0 = 7 / 5
rho_0 = 1.694 * 10 ** (-4)
P_0 = 1.013 * 10 ** 6
U_0 = 10 ** (-3)

gamma_3 = 7 / 5
C_3 = 3.6537 * 10 ** 4
P_3 = 1.6768 * 10 ** 6
U_3 = 1.229 * 10 ** 4

# Считаем коэффициенты уравнения
rho_3 = gamma_3 * P_3 / C_3 ** 2
X = P_3 / P_0
alpha_0 = (gamma_0 + 1) / (gamma_0 - 1)
n = 2 * gamma_3 / (gamma_3 - 1)
mu = (U_3 - U_0) * math.sqrt((gamma_0 - 1) * rho_0 / (2 * P_0))
nu = 2 / (gamma_3 - 1) * math.sqrt(gamma_3 * (gamma_0 - 1) / 2 * X * rho_0 / rho_3)

# Считаем коэффициенты а.
a_0 = X ** 2
a_1 = -alpha_0 * nu ** 2 * X
a_2 = 2 * alpha_0 * nu * (mu + nu) * X
a_3 = -(2 + (mu + nu) ** 2 * alpha_0) * X
a_4 = -nu ** 2
a_5 = 2 * nu * (mu + nu)
a_6 = -(nu + mu) ** 2 + 1

# Ищем значения А и В для основной теоремы алгебры

A = max(abs(a_1), abs(a_2), abs(a_3), abs(a_4), abs(a_5), abs(a_6))
B = max(abs(a_0), abs(a_1), abs(a_2), abs(a_3), abs(a_4), abs(a_5))

# Отрезок локализации [a,b]
a = abs(a_6) / (abs(a_6) + B)
b = 1 + A / abs(a_0)


# Функция для подсчета значения f(x) = a_0 * Z^14 + a_1 * Z^9 + a_2 * Z^8 + a_3 * Z^7 + a_4 * Z^2 + a_5 * Z + a_6
def f(x):
    y = a_0 * x ** 14 + a_1 * x ** 9 + a_2 * x ** 8 + a_3 * x ** 7 + a_4 * x ** 2 + a_5 * x + a_6
    return y


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


roots = [0, 0, 0]

for i in range(0, len(root_b)):
    roots[i] = precise_root(root_a[i], root_b[i])

# Находим значение давления P_1
P_1 = [roots[0] ** n * P_3, roots[1] ** n * P_3, roots[2] ** n * P_3]

# При P_1 = P[0]: -34583; =P[1]: -70727; =P[2]: 103078 => выбираем P[2]
P_1 = P_1[2]
U_1 = U_3 + 2 * C_3 / (gamma_3 - 1) * (1 - (P_1 / P_3) ** ((gamma_3 - 1) / (2 * gamma_3)))
D_0 = ((P_1 - P_0) / rho_0 + U_0 * (U_1 - U_0)) / (U_1 - U_0)

print(D_0)
