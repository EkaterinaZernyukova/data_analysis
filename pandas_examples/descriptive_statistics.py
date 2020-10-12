import pandas as pd
import numpy as np

d = {"Name": pd.Series(
    ["Andry", "Dik", "Tom", "Sit", "Anna", "Jim", "Andre", "lina", "Jorg", "Nik", "Lis", "Lida", "Helga"]),
    "Age": pd.Series([21, 23, 24, 25, 21, 23, 24, 25, 26, 37, 34, 32, 21]),
    "Rating": pd.Series([1.3, 1.4, 1.5, 1.6, 1.7, 1.2, 3.2, 2.1, 2.3, 4, 3.3, 2.2, 2.3])}
df = pd.DataFrame(d)
print(df)

print(df.sum())
print(df.mean())

print("Возвращает стандартное отклонение Бресселя (N-1) для числовых столбцов.")
print(df.std())

print("Функции описательной статистики в Python Pandas")
print(df.describe())
print(df.describe(include=["object"]))
print(df.describe(include="all"))