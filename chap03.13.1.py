import seaborn as sns
import pandas as pd
import numpy as np


df = sns.load_dataset('taxis')
print(df.head())
print()
print()


print(df.info())
print()
print()


df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])

print(df.info())
print()
print()


print(df['pickup'][0].year)
print()
print()


df['year'] = df['pickup'].dt.year
df['month'] = df['pickup'].dt.month
df['day'] = df['pickup'].dt.day

print(df[['pickup', 'year', 'month', 'day']].head())
print()
print()


df.sort_values('pickup', inplace=True)
df.reset_index(drop=True, inplace=True)

print(df.head())
print()
print()


print(df['dropoff'] - df['pickup'])
print()
print()


df.set_index('pickup', inplace=True)

print(df.head())
print()
print()


print(df.index)
print()
print()


print(df.loc['2019-02'])
print()
print()



print(df.loc['2019-03-01':'2019-03-02'])
print()
print()


#시계열 데이터 만들기

print(pd.date_range(start='2021-01-01', end='2021-12-31', freq='ME'))
print()
print()



print(pd.date_range(start='2021-01-01', end='2021-01-31', freq='3D'))
print()
print()


print(pd.date_range(start='2021-01-01', end='2021-01-31', freq='W-MON'))
print()
print()


print(pd.date_range(start='2021-01-01', end='2021-12-31', freq='WOM-2THU'))
print()
print()






