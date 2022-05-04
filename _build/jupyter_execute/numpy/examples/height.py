#!/usr/bin/env python
# coding: utf-8

# # Чему равен средний рост руководителей страны

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/height.csv')
data.head()


# In[3]:


data = data.rename(columns={"height(cm)":"height_cm"})
data.head(3)


# In[4]:


height_165 = data[data['height_cm'] > 165]
height_165.head(3)


# In[5]:


data.query("height_cm > 165")


# In[6]:


name_filter = 'Владимир Путин'


# In[7]:


data.query("name == @name_filter")


# In[ ]:





# In[8]:


data[data.name.str.contains("Екатерина")]


# In[9]:


data.name.str.lower().str.contains("екатерина")


# In[ ]:





# In[10]:


data['height(cm)'].values


# In[ ]:


heights = data['height(cm)'].values # np.array(data['height(cm)'])
print(heights)


# Теперь, получив такой массив данных, мы можем вычислить множество сводных статистических показателей:

# In[ ]:


print("Среднее:       ", heights.mean())
print("Стандартное отклонение:", heights.std())
print("Минимальный:    ", heights.min())
print("Максимальный:    ", heights.max())


# In[ ]:


print("25 процентиль:   ", np.percentile(heights, 25))
print("Медиана:            ", np.median(heights))
print("75 процентиль:   ", np.percentile(heights, 75))


# Иногда полезнее видеть графическое представление данных.

# In[ ]:


import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot style


# In[ ]:


plt.hist(heights)
plt.title('Распределение роста')
plt.xlabel('рост (см)')
plt.ylabel('число');


# In[ ]:




