#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# In[2]:


path = r'/home/artur/artur/study/university/Data Engineering/lab6/cars.csv'


# In[3]:


df = pd.read_csv(path)
df = df[['Make', 'Model', 'YEAR','(km)', 'CITY (kWh/100 km)',
    'HWY (kWh/100 km)', 'COMB (kWh/100 km)']].loc[df['YEAR']==2016]
df.reset_index(inplace = True)
del df['index']


# In[4]:


print(df.head())
print()
print(df.info())
print()
print(df.describe())


# In[5]:


def shapiro_wilk(column):
    data = df[column]
    print(column)
    stat, p = scipy.stats.shapiro(data)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')

    pyplot.hist(data, bins = 15)
    qqplot(data, line='s')
    pyplot.show()


# In[6]:


shapiro_wilk('(km)')


# In[7]:


shapiro_wilk('CITY (kWh/100 km)')


# In[8]:


shapiro_wilk('HWY (kWh/100 km)')


# In[9]:


shapiro_wilk('COMB (kWh/100 km)')


# In[ ]:




