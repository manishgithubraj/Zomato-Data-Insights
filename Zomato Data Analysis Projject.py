#!/usr/bin/env python
# coding: utf-8

# # zomato Data Analysis Using Python
# 

# # Step 1: Import necessary Python Libraries.

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# pandas is used to data manipulation and anlysis.
# numpy is used for numerical operations.
# matplotlib.pyplot and seaborn are used for data visulaization.
# 

# # Step 2 : Create the data frames

# In[2]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head)


# In[3]:


dataframe = pd.read_csv("Zomato data .csv")


# In[4]:


dataframe


# # let's convert the data type of the "rate" column to float and remove the denominator

# In[7]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head)


# # Summary of the dataframe

# In[8]:


dataframe.info


# # Conclusion - There is no NULL value in dataframe

# # Types of restaurant

# In[13]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("typs of restaurant")


# # Conclusion: The majority of the restaurant fall into the dining category.
# 
# 

# # Dining restaurant are preferred by a larger number of individuals.

# In[15]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="blue" , marker = "o")
plt.xlabel("Types of r restaurant", c="green", size = 20)
plt.ylabel("votes", c="green", size = 20)


# # Conclusion  - Dining restaurants has recieved maximum votes

# In[17]:


plt.hist(dataframe['rate'],bins = 5)
plt.title("Ratings Distribution")
plt.show()


# # Concl - The majority of the restauraunts recieved ratings ranging from 3.5 to 4.

# In[18]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # The majority of couples prefer restaurants with an approximate cost of 300 rupees.

# In[20]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate' , data = dataframe)


# # whether online orders receive higher ratings than offline orders

# In[21]:


pivot_table = dataframe.pivot_table(index = 'listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In(Type)")
plt.show()


# # CONCLUSION - Dining restaurants primarily accept offline orders , whereas cafes primarily receives online orders. This suggests thar client prefer to place orders in person at restaurants , but prefer online ordereing at cafes.

# In[ ]:




