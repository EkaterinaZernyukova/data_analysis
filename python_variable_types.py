
# range – диапазон
# str
# set – множество
# dict – словарь


def working_with_variables():
    int_variable = 100500
    print(int_variable)

    float_variable = 1.2
    print(float_variable)

    boo = 10 < int_variable
    print(boo)

    if (boo):
        print(f"'10' < '{int_variable}'")

    none_variable = None
    print(none_variable)
    none_variable = 23
    print(none_variable)

    if (none_variable == None):
        print("non_happens")
    else:
        print("happens")

    some_list_variable = list()
    print(some_list_variable)
    print(list())

    list_of_objects = [int_variable, float_variable, boo, none_variable, some_list_variable]
    print(list_of_objects)

    list_of_objects.append("new")
    print(list_of_objects)

    value = list_of_objects[0]
    print(value)

    print(f"Entrance count {list_of_objects.count('new')}")
