#!/usr/bin/env python
# coding: utf-8

import pandas as pd

path_to_data = r'/home/artur/artur/study/university/Data Engineering/lab1/LAbDAni_1'

data_csv = pd.read_csv(path_to_data + '/Schoollviv.csv', encoding='Windows-1251', sep=';')
print('\nData csv: \n', data_csv)

data_json = pd.read_json(path_to_data + '/renttherunway_final_data.json', lines=True)
print('\nData json: \n', data_json)

print('\n1. Розбити дані на 2 частини у співвідношенні 30% на 70%\n')

all_data_csv = len(data_csv.index)
print('data_csv 100% = ', all_data_csv)
len_thirty_data_csv = round(len(data_csv.index) * 0.3)
print('thirty_data_csv 30% = ', len_thirty_data_csv)
seventy_data_csv = all_data_csv - len_thirty_data_csv
print('seventy_data_csv 70% = ', seventy_data_csv)

tab1 = data_csv.loc[:len_thirty_data_csv - 1]
print('\nTable 1 (30%): \n', tab1)
tab2 = data_csv.loc[len_thirty_data_csv:]
print('\nTable 2 (70%): \n', tab2)

print('2. Об’єднати знов\n')
data_csv = pd.concat([tab1, tab2], ignore_index=True)
print('Concatenation: \n', data_csv)

print('\n3. Вибрати декілька колонок, рядків\n')
print('Conumns: \n', data_csv[['Назва', 'Кількість вихованців']])  # колонки
print('Rows: \n', data_csv.loc[1:3, :])  # рядки
print('Conumns & Rows: \n', data_csv.loc[:, :])  # рядки і колонки

print('4. Додати колонку, як комбінацію даних попередніх колонок\n')
combination_data_csv = data_csv['Назва'] + ' - ' + data_csv['Район']
data_csv['Комбінація'] = combination_data_csv
print('Add two columns: \n', data_csv)

print('5. Видалити непотрібні колонки')
data_csv.drop(columns=['Комбінація'], axis=1, inplace=True)
print('\nDrop column: \n', data_csv.columns)

print('\n6. Відсортувати по збільшенню і по зменшенню\n')
print('Sorting data[Кількість вихованців] in ascending: \n', data_csv.sort_values(by=['Кількість вихованців']), '\n')
print('Sorting data[Кількість вихованців] in descending order: \n',
      data_csv.sort_values(by=['Кількість вихованців'], ascending=False), '\n')
