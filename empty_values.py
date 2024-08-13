import pandas as pd

df = pd.read_csv('animal.csv')

print(df)

#df.fillna(0, inplace=True) # замена пустых значений таблицы на 0
#df.dropna(inplace=True) # удаление строк с пустыми значениями в таблице
#print(df)

#Группировка по значениям
#group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
#print(group)

#Сохранение изменений в файл
#df.to_csv('Output.csv', index=False)