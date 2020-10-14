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
# x = cos_grid
# y = sin_grid
# eps = 1e-6
# new = np.abs(x - y)<0.0005
# print(new)


def close(x, y, eps):
    x=cos_grid
    y=sin_grid
    eps=1e-6
    new=np.abs(x - y)
    if new < eps:
        print(True)
    else:
        return False

    # д) убедитесь, что все значения в полученном массиве равны True.
    result = np.abs(x - y) < 0.0005
    print(result)

# cardio_train_test = pd.read_csv(file_helper.get_resource_file_path("cardio_train.csv"))
# print(cardio_train_test.head())
#
# print(cardio_train_test.size)
# print(cardio_train_test.shape[1])
#
# # Второй столбец полученной матрицы обозначает возраст пациентов (в днях).
# # Переведите возраст в года, поделив на 365.25 и округлив вниз до ближайшего целого.
# # Замените соответствующий столбец в матрице.
