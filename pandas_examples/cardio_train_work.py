import pandas as pd
import numpy as np
from helpers import file_helper

# cardio_train_test = pd.read_csv(file_helper.get_resource_file_path("cardio_train.csv"), delimiter=';', skiprows=1)

cardio_train_test = np.loadtxt(file_helper.get_resource_file_path("cardio_train.csv"), delimiter=';', skiprows=1)

print(cardio_train_test)

print(cardio_train_test.size)
print(cardio_train_test.shape)

# Второй столбец полученной матрицы обозначает возраст пациентов (в днях).
# Переведите возраст в года, поделив на 365.25 и округлив вниз до ближайшего целого.
age_colomn = cardio_train_test[:, 1]
age_colomn = np.floor(age_colomn / 365.25)
print(age_colomn)

# Замените соответствующий столбец в матрице.
cardio_train_test[:, 1] = age_colomn
print(cardio_train_test)

print("Каково количество пациентов старше 50 лет?")
choose_age = age_colomn[age_colomn > 50]
print(choose_age.size)

# Третий столбец матрицы означает пол пациента (1 --- женщина, 2 --- мужчина).
# Четвёртый столбец соответствует росту. Верно ли, что средний рост мужчин больше среднего роста женщин?

print("Количество мужчин и женщин")
men_femal = cardio_train_test[:, 2]
print(men_femal[men_femal == 1].size)
print(men_femal[men_femal == 2].size)

# print("Количество мужчин и женщин")
# _size = (cardio_train_test[:, 2])
# men_size = _size[_size == 2]
# women_size = _size[_size == 1]
# print(men_size.size)
# print(women_size.size)
print("Средний рост мужчин")
medium_height_men = np.mean(cardio_train_test[:, 3][cardio_train_test[:, 2] == 2])
print(medium_height_men)
print("Средний рост женщин")
medium_height_women = np.mean(cardio_train_test[:, 3][cardio_train_test[:, 2] == 1])
print(medium_height_women)
print("Верно ли, что средний рост мужчин больше среднего роста женщин?")
medium_men_more = np.mean(cardio_train_test[:, 3][cardio_train_test[:, 2] == 2]) > np.mean(
    cardio_train_test[:, 3][cardio_train_test[:, 2] == 1])
print(medium_men_more)

# Пятый столбец означает вес человека. Каковы минимальный и максимальный вес в выборке?
# Какое количество людей имеют максимальный вес?
print("Максимальный вес")
print(np.max(cardio_train_test[:, 4]))
print("Минимальный вес")
print(np.min(cardio_train_test[:, 4]))
print("Людей с максимальным весом")
print(cardio_train_test[cardio_train_test[:, 4] == np.max(cardio_train_test[:, 4])].size)

# Каково количество некурящих людей (значение в четвёртом с конца столбце равно 0),
# у которых обнаружены сердечно-сосудистые заболевания (значение в последнем столбце равно 1)?
print(cardio_train_test[cardio_train_test[:, -4] == 0][:, -1][
          cardio_train_test[cardio_train_test[:, -4] == 0][:, -1] == 1].size)
