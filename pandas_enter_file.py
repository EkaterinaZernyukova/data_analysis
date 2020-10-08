import pandas as pn

# import titanic.csv
from helpers import file_helper

titanic_test = pn.read_csv(file_helper.get_resource_file_path("titanic.csv"))
print(titanic_test.head())
print(titanic_test.groupby(["Sex", "Survived"])["PassengerID"].count())
print(titanic_test.groupby(["PClass", "Survived"])["PassengerID"].count())
pvt = titanic_test.pivot_table(index=["Sex"], columns=["PClass"], values="Name", aggfunc="count")
print(pvt.loc["female", ["1st", "2nd", "3rd"]])


