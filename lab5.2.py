#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy.stats import norm 


# In[15]:


print('Task #1')


# In[70]:


data = {
    'milk' : [1, 3, 4, 7, 8],
    'meat' : [5, 4, 6, 9, 10],
    'poultry' : [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data)
print(df.corr())


# In[18]:


sns.jointplot(x='milk', y='meat', data=data, kind='scatter');
plt.xlabel('Milk')
plt.ylabel('poultry')
plt.show()


# In[19]:


sns.jointplot(x='milk', y='poultry', data=data, kind='scatter');
plt.xlabel('Milk')
plt.ylabel('Poultry')
plt.show()


# In[22]:


sns.jointplot(x='meat', y='poultry', data=data, kind='scatter');
plt.xlabel('Meat')
plt.ylabel('Poultry')
plt.show()


# In[26]:


print('Task #2')


# In[35]:


data = {
    'ec' : [2, 3, 1, 5, 4],
    'wc' : [1, 2, 3, 4, 5],
    'olympiad' : [3, 2, 1, 4, 5]
}


# In[36]:


df = pd.DataFrame(data)
df.index += 1
print(df.corr())


# In[47]:


sns.jointplot(x='ec', y='wc', data=data, kind='scatter');
plt.xlabel('ec')
plt.ylabel('wc')
plt.show()


# In[44]:


sns.jointplot(x='ec', y='olympiad', data=data, kind='scatter');
plt.xlabel('ec')
plt.ylabel('olympiad')
plt.show()


# In[45]:


sns.jointplot(x='wc', y='olympiad', data=data, kind='scatter');
plt.xlabel('wc')
plt.ylabel('olympiad')
plt.show()


# In[49]:


print('Task #3')


# In[65]:


path_to_data = r'/home/artur/artur/study/university/Data Engineering/lab5/Schoollviv.csv'
data = pd.read_csv(path_to_data, encoding='Windows-1251', sep = ';')
print(data.head(1))
print('\n')
print(data.corr())


# In[66]:


sns.jointplot(x = 'Кількість гуртків', y = 'Кількість вихованців', data=data, kind='scatter');
plt.show()


# In[ ]:





# In[72]:


data = {
    'milk' : [1, 3, 4, 7, 8],
    'meat' : [5, 4, 6, 9, 10],
    'poultry' : [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data)
print(df.corr())


# In[73]:


milk = df['milk']
meat = df['meat']
poultry = df['poultry']


# In[74]:


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


# In[75]:


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


# In[76]:


average_numbers_milk = np.array(average_numbers_milk)
average_numbers_meat = np.array(average_numbers_meat)
average_numbers_milk_meat = (average_numbers_milk * average_numbers_meat)
suma_average_numbers_milk_meat = sum(average_numbers_milk_meat)
result = suma_average_numbers_milk_meat / np.sqrt(suma_average_numbers_power_milk * suma_average_numbers_power_meat)
print('Correlation Milk-Meat or Meat-Milk: ', result)


# In[ ]:




