#!/usr/bin/env python
# coding: utf-8

# # Операции над картинками

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


get_ipython().system('wget https://dfedorov.spb.ru/python3/book_urite.jpg')


# In[3]:


image = plt.imread("book_urite.jpg")
plt.imshow(image)


# In[4]:


type(image)


# In[5]:


plt.imshow(image + 50)


# In[6]:


plt.imshow(image // 2)


# In[7]:


plt.imshow(np.cos(np.pi / 2 * image / 255))


# In[8]:


image.shape


# In[9]:


image_trans = np.transpose(image, (1, 0, 2))
print(image_trans.shape)
plt.imshow(image_trans)


# In[10]:


plt.imshow(image[100:, :200])


# In[ ]:




