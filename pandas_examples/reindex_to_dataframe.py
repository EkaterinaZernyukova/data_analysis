import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame({"A": pd.date_range(start="2016-01-01", periods=N, freq="D"),
                   "X": np.linspace(0, stop=N - 1, num=N),
                   "Y": np.random.rand(N),
                   "C": np.random.choice(["Low", "Medium", "High"], N).tolist(),
                   "D": np.random.normal(100, 10, size=(N)).tolist()
                   })
print("Reindex the DataFrame")
df_reindex = df.reindex(index=[0, 2, 5], columns=["A", "C", "B"])
print(df_reindex)

df1 = pd.DataFrame(np.random.randn(10, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])
df1 = df1.reindex_like(df2)

print(df1)

print(df2.reindex_like(df1))

print("Data Frame with Forward Fill:")
print(df2.reindex_like(df1, method='ffill'))
