#!/usr/bin/env python
# coding: utf-8

# # Deaths by Tuberculosis
# by Craig Warren 03 August 2019
# This is my first project for the first part of The Open University's _Learn to code for Data Analysis_ course.

# **Tuberculosis** (TB) is a bacterial infection spread through inhaling tiny droplets from the coughs or sneezes of an infected person. It is a serious condition, but can be cured with proper treatment. TB mainly affects the lungs. However, it can affect any part of the body, including the glands, bones and nervous system.
# TB does not make the news headlines like other epidemics such as Ebola or SARS, but TB is far more deadly.

# The source of the data used in this project is the World Health Organization(WHO). If you would like to learn about what the WHO does, you can go to [The World Health Organization](https://www.who.int/)

# Given the population and number of deaths due to TB in some countries during one year, the following questions will be answered:
# * What is the total, maximum, minimum and average number of deaths in that year?
# * Which countries have the most and the least deaths?
# * What is the death rate (deaths per 100,000 inhabitants) for each country?
# * Which countries have the lowest and highest death rate?

# ## The Data

# The data consists of total population and total number of deaths due to TB (excluding HIV) in 2013 in all of the countries in the world.
# The data was taken in August 2019 from http://apps.who.int/gho/data/node.main.POP107?lang=en (population) and http://apps.who.int/gho/data/node.main.1317?lang=en (deaths). The uncertainty bounds of the number of deaths were ignored.
# The data was collected into an Excel file.

# In[1]:


import warnings
warnings.simplefilter('ignore', FutureWarning)
from pandas import *
data_frame = read_excel('WHO POP TB all.xls')
print(data_frame)


# ### The range of the problem
# The column of interest is the last column in the data frame, _**TB deaths**_.

# In[3]:


tbd_col = data_frame['TB deaths']
print(tbd_col)


# The total number of deaths in 2013 is:

# In[4]:


total_deaths = tbd_col.sum()
print(total_deaths)


# The largest and smallest number of deaths in a single country are:

# In[5]:


largest_number_deaths = tbd_col.max()
print(largest_number_deaths)


# In[7]:


smallest_number_deaths = tbd_col.min()
print(smallest_number_deaths)


# From less 0.0 to almost a quarter of a million deaths is a huge range. The average number of deaths, over all countries in the data, can give a better idea of the seriousness of the problem in each country. The average can be computed as the mean or the median. Given the wide range of deaths, the median is probably a more sensible average measure.

# In[8]:


mean_average = tbd_col.mean()
print(mean_average)


# In[10]:


median_average = tbd_col.median()
print(median_average)


# The median is far lower than the mean. This indicates that some of the countries had a very high number of TB deaths in 2013, pushing the value of the mean up.

# ### The most affected 
# To see the most affected countries, the table is sorted in ascending order by the last column, which puts those countries in the last rows.

# In[12]:


deaths_sort = data_frame.sort_values('TB deaths')
print(deaths_sort)


# The table raises the possibility that a large number of deaths may be partly due to a large population. To compare the countries on an equal footing, the death rate per 100,000 inhabitants is computed.

# In[16]:


population_col = data_frame['Population (1000s)']
data_frame['TB deaths (per 100,000)'] = tbd_col * 100 / population_col
print(data_frame)


# ### Conclusions 

# The worlds countries had a total of about 10777.97 deaths due to TB in 2013. The median shows that half of these coutries had fewer than 315.0 deaths. The much higher mean (over 5500) indicates that some countries had a very high number. The least affected were San Marino, Niue and Monaco, with 0.00, 0.01 and 0.03 deaths respectively, and the most affected were Nigeria and India with over 17 thousand and over 1 million and 250 thousand deaths respectively in a single year.
# 
# Most values are estimates, but nevertheless, they convey the message that TB is still a major cause of fatalities, and that there is a huge disparity between countries, with several countries being highly affected.




