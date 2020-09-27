# str
# set – множество
# dict – словарь


def working_with_variables():
    first_variable = 10
    second_number = 3
    print(first_variable + second_number)
    first_variable += second_number
    print(first_variable)

    print(first_variable - second_number)
    print(first_variable / second_number)
    print(first_variable * second_number)

    first_variable *= second_number  # first_variable = first_variable * 10
    print(first_variable)

    round_variable = first_variable // second_number

    print(f"First variable {first_variable} Second variable {second_number}")
    print(round_variable)

    print(first_variable % second_number)
    print(second_number ** first_variable)

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

    for i in range(3, 16, 3):
        quotient = i / 3
        print(f"{i} делится на 3, результат {int(quotient)}.")
