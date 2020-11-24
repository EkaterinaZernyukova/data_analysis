import numpy as np

# data = np.ones(3)
data = np.array([1, 2, 3, ])
print(data)

data_first = np.ones((3, 2))
print(data_first)

data_second = np.zeros((3, 2))
print(data_second)

data_ran = np.random.random((3, 2))
print(data_ran)

print(data_ran / 1.5)
# new_date = (data_first / data_second)
# print(new_date)

try:
    print("Data first: ")
    print(data_first)
    print("Data second: ")
    print(data_second)
    result = data_first / data_second
    print("--- Все ок ---")
    print(f"Result: {result}")
except BaseException as error:
    print(f"Ошибка при делении матриц {error}")

print(data.max())
print(data.sum())
print(data.min())
print(data.mean())
print(data.prod())
print(data.std())

print("Агрегирование")
print(data_ran.max(axis=0))
print(data_ran.min(axis=1))


new_list_dates = np.array([[1, 2], [3, 4],[5,6],[8,9]])
print(new_list_dates)

print("Транспортирование")
print(new_list_dates.T)
print(new_list_dates.reshape(4,2))



