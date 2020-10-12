import pandas as pd
import numpy as np

# Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print(s)

print("The axes are:")
print(s.axes)

print("Is the Object empty?")
print(s.empty)

print("The dimensions of the object:")
print(s.ndim)

print("The size of the object:")
print(s.size)

# Возвращает фактические данные в серии в виде массива:
print("The actual data series is:")
print(s.values)

print("The first two rows of the data series:")
print(s.head(2))

print("The last two rows of the data series:")
print(s.tail(2))

# Create a Dictionary of series
d = {"Name": pd.Series(["Tom", "Jane", "Lucia", "Fox", "Engel", "Glory", "Stiv"]),
     "Age": pd.Series([23, 24, 23, 22, 21, 25, 40]),
     "Rating": pd.Series([1.2, 1, 4.5, 3.2, 4, 1, 1.2])}
# Create a DataFrame
df = pd.DataFrame(d)
print(df)

print("The transpose of the data series is:")
print(df.T)

print("Row axis labels and column axis labels are:")
print(df.axes)

print("The data types of each column are:")
print(df.dtypes)

print("Is the object empty?")
print(df.empty)

# Количество измерений объекта
print(df.ndim)

print ("The shape of the object is:")
print(df.shape)

print ("The total number of elements in our object is:")
print(df.size)

print ("The actual data in our data frame is:")
print(df.values)

print(df.head(3))
print(df.tail(2))