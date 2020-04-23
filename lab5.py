#!/usr/bin/env python
# coding: utf-8

import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

print('Task #1')

data = {
    'milk' : [1, 3, 4, 7, 8],
    'meat' : [5, 4, 6, 9, 10],
    'poultry' : [5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

print(df.corr())

milk = df['milk']
meat = df['meat']
poultry = df['poultry']

######################## ПОШУК КОРЕЛЯЦІЇ БЕЗ corr()

average_numbers_milk = []
average_numbers_power_milk = []

print('sum: ', milk.sum())
average_milk = milk.mean()
print('average:', average_milk)
for i in milk:
    average_numbers_milk.append(average_milk - i)
    average_numbers_power_milk.append((average_milk - i) ** 2)

suma_average_numbers_power_milk = sum(average_numbers_power_milk)
print(suma_average_numbers_power_milk)

average_numbers_meat = []
average_numbers_power_meat = []

print('sum: ', meat.sum())
average_meat = meat.mean()
print('average:', average_meat)
for i in meat:
    average_numbers_meat.append(average_meat - i)
    average_numbers_power_meat.append((average_meat - i) ** 2)

suma_average_numbers_power_meat = sum(average_numbers_power_meat)
print(suma_average_numbers_power_meat)

average_numbers_milk = np.array(average_numbers_milk)
average_numbers_meat = np.array(average_numbers_meat)
average_numbers_milk_meat = (average_numbers_milk * average_numbers_meat)
suma_average_numbers_milk_meat = sum(average_numbers_milk_meat)
result = suma_average_numbers_milk_meat / np.sqrt(suma_average_numbers_power_milk * suma_average_numbers_power_meat)
print('Correlation Milk-Meat or Meat-Milk: ', result)

################################################

print('Task #2')

data = {
    'ec' : [2, 3, 1, 5, 4],
    'wc' : [1, 2, 3, 4, 5],
    'olympiad' : [3, 2, 1, 4, 5]
}

df = pd.DataFrame(data)
df.index += 1
print(df)
print(df.corr())

print('Task #3')

path_to_data = r'/home/artur/artur/study/university/Data Engineering/lab1/LAbDAni_1'
data = pd.read_csv(path_to_data + '/Schoollviv.csv', encoding='Windows-1251', sep = ';')
print(data.shape)

print(data['Кількість вихованців'].describe())
print('\n')
print(data.info())

plt.figure(figsize = (9, 5)) 
data['Кількість вихованців'].plot(kind ="hist") 

corrmat = data.corr() 
  
f, ax = plt.subplots(figsize =(9, 8)) 
sns.heatmap(corrmat, ax = ax, cmap ="YlGnBu", linewidths = 0.1) 

corrmat = data.corr() 

cg = sns.clustermap(corrmat, cmap ="YlGnBu", linewidths = 0.1); 
plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation = 0) 

k = 15

cols = corrmat.nlargest(k, 'Кількість вихованців')['Кількість вихованців'].index 

cm = np.corrcoef(data[cols].values.T) 
f, ax = plt.subplots(figsize =(12, 10)) 

sns.heatmap(cm, ax = ax, cmap ="YlGnBu", 
            linewidths = 0.1, yticklabels = cols.values, 
                            xticklabels = cols.values) 

plt.show()
