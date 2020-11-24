import pandas as pd
import numpy as np

date = [1,5,2,7,1,9,3,8,5,9]
pf = pd.DataFrame(date)
print(pf)



date = [["Mark", 12], ["Yuri", 6], ["Misha", 8]]
pf2 = pd.DataFrame(date, columns=["Name", "Age"], dtype=float)
print(pf2)

date = {"Name": ["Kate", "Sonya", "Ylia", "Morty"], "Age": [13, 15, 17, 10]}
pf3 = pd.DataFrame(date, index=["mumia1", "mumia2", "mumia3", "mumia4"])
print(pf3)

date = [{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 8}]
pf4 = pd.DataFrame(date, index=["first", "second"], columns=["a", "b"])
pf5 = pd.DataFrame(date, index=["first", "second"], columns=["a", "b1"])
print(pf4)
print(pf5)

d = {"one": pd.Series([1, 2, 3], index=["a", "b", "c"]),
     "two": pd.Series([6, 7, 8, 9], index=["a", "b", "c", "d"])}
pf1 = pd.DataFrame(d)
print(pf1)
print(pf1["one"])

print("Adding a new column by passing as Series:")
pf1["three"] = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(pf1)

print("Adding a new column using the existing columns in DataFrame:")
pf1["four"] = pf1["one"] + pf1["three"]
print(pf1)

print("Using the previous DataFrame, we will delete a column")
del pf1["one"]
print(pf1)

print("Deleting another column using POP function:")
pf1.pop("two")
print(pf1)

print("Строки могут быть выбраны путем передачи метки строки в функцию loc")
print(pf1.loc["b"])

print("Строки можно выбирать, передавая целочисленное местоположение в функцию iloc")
print(pf1.iloc[3])

print("Выбор нескольких строк")
print(pf1[0:2])

print("Добавить строки в конце")
nw = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
nw2 = pd.DataFrame([[5, 6], [7, 8]], columns=["c", "d"])
nw = nw.append(nw2)
print(nw)

print("Drop rows with label 0")
nw = nw.drop(1)
print(nw)

print("Структура данных Series")
s = pd.Series()
print(s)
data = np.array(["a", "b", "c", "d"])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)

data = {"a": 0., "b": 1., "c": 2.}
s = pd.Series(data, index=["b", "c", "d", "a"])
print(s)

s = pd.Series([5, 6, 7, 8, 9, "a"], index=[0, 1, 2, 3, 4, 5])
print(s[:3])
print(s[-4:])

print("Получить один элемент, используя значение метки индекса.")
print(s[5])
print(s[[5, 2]])
