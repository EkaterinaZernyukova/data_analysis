import pandas as pd
import numpy as np

print("Инициализация MultiIndexes.")

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
print(tuples)

index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
print(index)

s = pd.Series(np.random.randn(8), index=index)
print(s)

print("Передать список массивов напрямую Seriesили DataFrame")
s = pd.Series(np.random.randn(8), index=arrays)
print(s)

df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
print(df)
#
# iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
# index = pd.MultiIndex.from_product(iterables, names=['first', 'second'])
# print(index)
#
# df = pd.DataFrame([["bar", "one"], ["bar", "two"], ["baz", "one"], ["baz", "two"]], columns=["first", "second"])
# result = pd.MultiIndex.from_frame(df)
# print(result)
#
# print("Cтроковые имена для самих уровней.")
# FrozenList = df.index.names
# print(FrozenList)
#
# print("Количество уровней индекса")
# df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
# print(df)
#
# result = pd.DataFrame(np.random.randn(6, 6), index=index[:6], columns=index[:6])
# print(result)

# print("Разрезаны верхнии уровни индексов")
# with pd.option_context('display.multi_sparse', False):
#     df
# # print(df)
# # df = pd.Series(np.random.randn(8), index=tuples)
# # print(df)
# # #
# # df = index.get_level_values(0)
# # print(df)
# # df = index.get_level_values('second')
# # print(df)
#
# print("Иерархическое индексирование ")
# new = df.columns.levels
# print(new)
# new = df[['foo', 'qux']].columns.levels
# print(new)
# new = df[['foo', 'qux']].columns.to_numpy()
# print(new)

# print("Видеть только используемые уровни")
# new = df[['foo', 'qux']].columns.get_level_values(0)
# print(new)
#
# print("Для восстановления MultiIndex")
# new = df[['foo', 'qux']].columns.remove_unused_levels()
# print(new)
# print(new.levels)
print("Filter")
new = df.loc['bar','one']
print(new)


