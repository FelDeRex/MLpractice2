import pandas as pd
import matplotlib as plt

df = pd.read_csv("H1N1_Flu_Vaccines.csv", sep=',')
df.head(10)

df = df.drop_duplicates(subset='hhs_geo_region')
df = df[df['education'] == 'College Graduate']
df.dropna(axis=0, how='all')

print(df)

print('Максимальное число детей:', max(df['household_children']))
print('Среднее число детей:', df['household_children'].mean())
print('Среднее квадратичное отклонение числа детей:', df['household_children'].std())