import pandas as pd

df = pd.read_csv('salary_data.csv')

print(df.head())

print(df.info())

print(df.describe())