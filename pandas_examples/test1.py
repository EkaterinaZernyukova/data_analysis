import pandas as pd
import numpy as np
from helpers import file_helper

cardio_train_test = pd.read_csv(file_helper.get_resource_file_path("cardio_train.csv"),delimiter=';',skiprows=1)

# cardio_train_test=np.loadtxt(file_helper.get_resource_file_path("cardio_train.csv"), delimiter=';', skiprows=1)

print(cardio_train_test)

print(cardio_train_test.size)
print(cardio_train_test.shape)
#
# # Второй столбец полученной матрицы обозначает возраст пациентов (в днях).
# # Переведите возраст в года, поделив на 365.25 и округлив вниз до ближайшего целого.
# # Замените соответствующий столбец в матрице.
