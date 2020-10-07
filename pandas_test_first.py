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

my_wish_list3.index=["N","I","K","I"]
print(my_wish_list3)

