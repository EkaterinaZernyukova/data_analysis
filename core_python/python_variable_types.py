# str
# set – множество
# dict – словарь


def working_with_variables():
    first_variable: int = 10
    second_number: int = 3
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

    float_variable: float = 1.2
    print(float_variable)

    boo = 10 < first_variable
    print(boo)

    if (boo):
        print(f"'10' < '{first_variable}'")

    none_variable: None = None
    print(none_variable)
    none_variable = 23
    print(none_variable)

    print("Внимание")

    if (none_variable == None):
        print("non_happens")
    else:
        print("happens")

    some_list_variable = list()
    print(some_list_variable)
    print(list())

    list_of_objects = [first_variable, float_variable, boo, none_variable, some_list_variable]
    print(list_of_objects)

    list_of_objects.append("new")
    print(list_of_objects)

    value = list_of_objects[0]
    print(value)

    print(f"Entrance count {list_of_objects.count('new')}")

    for i in range(3, 16, 3):
        quotient = i / 3
        print(f"{i} делится на 3, результат {int(quotient)}.")

working_with_variables()

def working_with_variables_2():
    not_tab_string: str = r"\t"
    print(not_tab_string)

    integer_list = [1, 2, 3]
    haterogeneous_list = ["строка", 0.1, True]
    list_of_list = [integer_list, haterogeneous_list, []]
    list_length = len(integer_list)
    list_sum = (integer_list)
    if 0.1 in haterogeneous_list:
        print()
    integer_list.extend([3, 4, 5])
    print(len(integer_list))

    my_list = [1, 2]
    my_list[0] = 6
    print(my_list)

    my_tuple: tuple = (1, 2, 8)
    other_tuple = 1, 2, 3
    print(other_tuple)

    empty_dict = {}
    empty_dict["kate"] = 10
    empty_dict["nil"] = 8
    empty_dict["lo"] = 1234
    print(empty_dict)

    Kate_has = "kate" in empty_dict
    print(Kate_has)

working_with_variables_2()
#
x = 10
print(x)
y = 12
print(y)

tuple_coordinates = (x, y)
print(tuple_coordinates)

def sum_and_product(coordinates: tuple):
    if (len(coordinates) != 2):
        print("Passed tuple has not exactly 2 coordinates")
        return

    x_coord = coordinates[0]
    y_coord = coordinates[1]

    print(f"X coordinate of tuple is: '{x_coord}'")
    print(f"Y coordinate of tuple is: '{y_coord}'")


def sum_and_product(x: int, y: int):
    x_coordinate = x + y
    y_coordinate = x * y

    return (x_coordinate, y_coordinate)
    result = (x + y), (x * y)
    print(result)
    # return result


# result = sum_and_product(1, 3)
# print(result)
# #
# #     sp = sum_and_product(2, 3)
# #     print(sp)
# #
# #     s, p = sum_and_product(5, 10)
# #     print(s, p)
