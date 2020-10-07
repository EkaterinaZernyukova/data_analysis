import pandas as pn

my_wish_list = pn.Series([1, 3, 5, 6.6, 5.5, 567])
print(my_wish_list)
print(my_wish_list.index)

print("Список элементов")
print(my_wish_list.values)
print(my_wish_list[4])

my_wish_list2 = pn.Series([16, 4, 26, 33.4, 56, 78], index=["a", "b", "c", "d", "e", "f"])
print(my_wish_list2[["b", "a", "c"]])
my_wish_list2[["d", "e"]] = 234
print(my_wish_list2)

print("Операции с Series")
print(my_wish_list2[my_wish_list2 < 20] * 2)

my_wish_list3 = pn.Series({"k": 23, "a": 25, "t": 14, "e": 233})
print(my_wish_list3)
print("chek")
print("k" in my_wish_list3)
print("k" + "a")
my_wish_list3[["k"]] = 32
print(my_wish_list3)
print("k" > "a")

my_wish_list3.name = "numbers"
my_wish_list3.index.name = "letters"
print(my_wish_list3)

my_wish_list3.index = ["N", "I", "K", "I"]
print(my_wish_list3)

print("work with DataFrame")
my_vocabulary1 = pn.DataFrame({"country": ["Italia", "USA", "Portugal"], "rater": [20, 50, 80], "food": ["pizza",
                                                                                                         "burger",
                                                                                                         "anona"]},
                              index=["I", "U", "P"])
print(my_vocabulary1["rater"])
print(type(my_vocabulary1["rater"]))

print(my_vocabulary1.columns)
print(my_vocabulary1.index)
my_vocabulary1.index.name = "favorit"
print(my_vocabulary1)

print("доступ к строкам")
print(my_vocabulary1.loc[["U"], "food"])
print(my_vocabulary1.iloc[2])

print("слайсинг")
print(my_vocabulary1.loc["I":"P", :])

print("фильтр по буллевому значению")
print(my_vocabulary1[my_vocabulary1.rater > 49][["country"]])

print("добавить столбец")
my_vocabulary1["price"] = my_vocabulary1["rater"] * 0.1
print(my_vocabulary1)

print("Удалить столбец")
my_vocabulary1 = my_vocabulary1.drop(["rater"], axis="columns")
print(my_vocabulary1)
#
# del my_vocabulary1["food"]
# print(my_vocabulary1)
#
# print("сбросить индексы")
# print(my_vocabulary1.reset_index())
