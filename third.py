import pandas as pd

df = pd.read_csv('hh.csv')

df['Test'] = [new for new in range(len(df))] # добавление нового столбца c индексами строк

print(df)

df.drop('Test', axis=1, inplace=True)
# удаление столбца (axis=1), inplace=True - обновление исходного датафрейма,
# (axis=0) - удаление строки, inplace=False - не обновляет исходный датафрейм, возвращает новый

print(df)

df.drop(49, axis=0, inplace=True)
# (axis=0) - удаление строки с индексом 49

print(df)
