#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print('\n')
print('Lab 3-4')
print('\n')

path_to_data = r'/home/artur/artur/study/university/Data Engineering/lab1/LAbDAni_1'
data = pd.read_csv(path_to_data + '/Schoollviv.csv', encoding='Windows-1251', sep = ';')
data = data.drop(index = 15)

print('data.head()')
print(data.head())
print('\n')

print('data.info()')
print(data.info())
print('\n')

print('data.descrive()')
print(data.describe())
print('\n')


def ames_eda(df): 
    eda_df = {}
    eda_df['null_sum'] = df.isnull().sum()
    eda_df['null_pct'] = df.isnull().mean()
    eda_df['dtypes'] = df.dtypes
    eda_df['count'] = df.count()
    eda_df['mean'] = df.mean()
    eda_df['median'] = df.median()
    eda_df['min'] = df.min()
    eda_df['max'] = df.max()
    
    return pd.DataFrame(eda_df)

print('ames_eda(data)')
print(ames_eda(data))
print('\n')

print("data.select_dtypes(include = ['object']).columns")
print(data.select_dtypes(include = ['object']).columns)
print('\n')

print('correlations')
correlations = data.corrwith(data['Кількість вихованців']).iloc[:-1].to_frame()
correlations['abs'] = correlations[0].abs()
sorted_correlations = correlations.sort_values('abs', ascending=False)[0]
print(sorted_correlations)
print('\n')


sns.set(style='whitegrid')
plt.figure(figsize=(10,8))
ax = sns.boxplot(x='Кількість вихованців', data=data, orient="v")
plt.show()


data = data.dropna(subset = ['Кількість вихованців'])
plt.figure(figsize=(14,8))
sns.distplot(data['Кількість вихованців'], kde=False)
plt.show()


