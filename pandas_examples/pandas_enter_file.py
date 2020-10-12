import pandas as pn
import matplotlib.pyplot as ml

# import titanic.csv
from helpers import file_helper

titanic_test = pn.read_csv(file_helper.get_resource_file_path("titanic.csv"))
print(titanic_test.head())
print(titanic_test.groupby(["Sex", "Survived"])["PassengerID"].count())
print(titanic_test.groupby(["PClass", "Survived"])["PassengerID"].count())
pvt = titanic_test.pivot_table(index=["Sex"], columns=["PClass"], values="Name", aggfunc="count")
print(pvt.loc["female", ["1st", "2nd", "3rd"]])

apple_test = pn.read_csv(file_helper.get_resource_file_path("apple.csv"), index_col="Date", parse_dates=True)
apple_test = apple_test.sort_index()
print(apple_test.info())
print(apple_test.loc["2012-Feb", "Close"].mean())
print(apple_test.loc["2012-Feb":"2015-Feb", "Close"].mean())
print(apple_test.resample("W")["Close"].mean())

for_view = apple_test.loc["2012-Feb":"2017-Feb", "Close"]
for_view.plot()
ml.show()
