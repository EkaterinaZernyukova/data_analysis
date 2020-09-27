
# list – список
# tuple – кортеж
# range – диапазон
# Строки (Text Sequence Type )
# str
# Бинарные списки (Binary Sequence Types)
# bytes – байты
# bytearray – массивы байт
# memoryview – специальные объекты для доступа к внутренним данным объекта через protocol buffer
# Множества (Set Types)
# set – множество
# frozenset – неизменяемое множество
# Словари (Mapping Types)
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
    else: print("happens")