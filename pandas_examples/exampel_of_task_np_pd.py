import numpy as np
import pandas as pd

print(np.__version__)
from helpers import file_helper

x = np.zeros(10)
print(x)
x[4] = 1
print(x)
x[-3:] = 2
print(x)

# "Создайте выборку (одномерный массив) значений роста для 100 человек из равномерного распределения на отрезке  [150;200]"
gros = np.random.uniform(150, 200, 100)
print(gros)

# средний рост людей по выборке μ
gros_mean = gros.mean()
print(gros_mean)

# стандартное отклонение σ
gros_standart = gros.std()
print(gros_standart)

# Удалите "аномальные" (не подчиняющиеся правилу выше) значения роста из выборки.
# Какой процент людей в выборке имеют рост в диапазоне  [μ−3σ;μ+3σ]
gros_unic = gros[(gros >= gros_mean - gros_standart) & (gros <= gros_mean + gros_standart)]
print(gros_unic)
print(gros_unic.size)
print(gros_unic.size / gros.size)

# Создайте равномерную сетку из 20 точек на отрезке  [0;π2]
grid = np.linspace(0, np.pi / 2, 20)
print(grid)

# Проверьте для каждой точки выполнение тригонометрического тождества  cosα=sin(π2−α)
# Для этого:
# а) создайте массив  cosα ;
cos_grid = np.cos(grid)
print(cos_grid)

# б) создайте массив  sin(π2−α) ;
sin_grid = np.sin(np.pi / 2 - grid)
print(sin_grid)

# Проверьте для каждой точки выполнение тригонометрического тождества  cosα=sin(π2−α)
print(cos_grid - sin_grid)

# в) создайте логическую функцию close(x, y, eps), которая возвращает True, если  |x−y|<ε , и False в противном случае;
# г) примените данную функцию к двум массивам, созданным выше;
print("Логическая функция")


def close(x, y, eps):
    return np.abs(x - y) < eps


print(close(cos_grid, sin_grid, 1e-6))

# # д) убедитесь, что все значения в полученном массиве равны True.
# Во всех языках программирования 1е-6 это = 0,000 001. Это 1 умножить на 10 в минус шестой степени - сокращенная запись.
# E (exponent) — буква E, означающая «*10^»


close_vector = np.vectorize(close)
print(close_vector(cos_grid, sin_grid, 0.0000000000000000000000000000000000000000005))

# Создайте матрицу (двумерный массив) из нормального распределения с параметрами  μ=5 ,  σ=2.5  размером  10×5
#  Выборка из нормального распределения со средним 5, стандартным отклонением 2.5
matrica = np.random.normal(5, 2.5, (10, 5))
print(matrica)

# Найдите среднее значение в 5-й строке.
print("5я строка")
print(matrica[4])
print(matrica[4, :])
print(np.mean(matrica[4:]))

# Найдите медиану 3-го столбца.
print("3й столбец")
print(matrica[:, 2])
print(np.median(matrica[:, 2]))

# Посчитайте сумму элементов матрицы: а) по строкам; б) по столбцам; в) сумму всех элементов.
print("Суммы")
print(np.sum(matrica, axis=1))
print(np.sum(matrica, axis=0))
print(np.sum(matrica))

# Вычислите определитель (детерминант) подматрицы размером  3×3 , расположенной в левом верхнем углу исходной матрицы.
# Вычисление определителя нужно чтобы узнать, обратима ли матрица.
# Узнавать, обратима ли матрица, нужно для того, чтобы решить: обращать её таки - а это сложная алгоритмическая задача - или нет.
# Обращать матрицы нужно для вычисления коэффициентов линейной регрессии.
# А линейная регрессия - один из основных инструментов в статистике, которая нужна для предсказания результатов.
print(matrica[:3, :3])
print(np.linalg.det(matrica[:3, :3]))

print("Обратная матрица")
print(np.linalg.inv(matrica[:3, :3]))

# Найдите количество строк с суммой элементов меньше средней суммы по строкам.

# print([np.sum(matrica, axis=1) < np.mean(matrica, axis=1)])
# print("Средняя сумма по строкам")
# print(np.mean(matrica, axis=1))
# print("Сумма элементов по строкам")
# print(np.sum(matrica, axis=1))
# print(np.shape(matrica[0]))
sum_middle_line = np.sum(matrica, axis=1)
print("Сумма по строкам")
print(sum_middle_line)
mean_sum_middle_line = np.mean(sum_middle_line)
print("Среднее")
print(mean_sum_middle_line)
print("Сравнение")
print(sum_middle_line < mean_sum_middle_line)
list_sum = sum_middle_line[sum_middle_line < mean_sum_middle_line]
print(list_sum)
print(list_sum.shape[0])

# Выделите из матрицы строки по правилу: значение первого элемента больше последнего. Найдите размеры полученной матрицы.
first_more = (matrica[matrica[:, 0] > matrica[:, -1], :])
print(first_more)
print("Вся первая строка")
print(matrica[0, :])
print(matrica[0])

print(first_more.shape, first_more.ndim)

# Найдите ранг матрицы, построенной по правилу: сумма элементов строки выше средней суммы по строкам.
list_sum = sum_middle_line[sum_middle_line > mean_sum_middle_line]
print(list_sum)
print(list_sum.shape[0])
print(np.linalg.matrix_rank(list_sum))
