import pandas as pn
# import titanic.csv
from helpers import file_helper

titanic_test=pn.read_csv(file_helper.get_resource_file_path("titanic.csv"))
print(titanic_test.head())

