import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
print(df)

# (df.head(3)) - вывод первых трех строк
# (df.tail(3)) - вывод последних трех строк
# (df.info()) - вывод информации о датафрейме
# (df.describe()) - вывод описательной статистики
# (df.columns) - вывод названий столбцов
# df['Country name'] - вывод столбца с названием страны
# df[['Country name', 'Regional indicator']] - вывод столбцов с названием страны и региона
# df.loc[3] - вывод строки с индексом 3
# df.loc[3, 'Country name'] - вывод строки с индексом 3 и столбца с названием страны
# df[df['Healthy life expectancy'] > 0.8] - вывод строк с жизней счастья больше 0.8
# df[df['Healthy life expectancy'] < 0.8] - вывод строк с жизней счастья меньше 0.8