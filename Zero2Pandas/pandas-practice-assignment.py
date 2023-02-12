#!/usr/bin/env python
# coding: utf-8

# # Assignment 3 - Pandas Data Analysis Practice
# 
# *This assignment is a part of the course ["Data Analysis with Python: Zero to Pandas"](https://jovian.ai/learn/data-analysis-with-python-zero-to-pandas)*
# 
# In this assignment, you'll get to practice some of the concepts and skills covered in this tutorial: https://jovian.ai/aakashns/python-pandas-data-analysis
# 
# As you go through this notebook, you will find a **???** in certain places. To complete this assignment, you must replace all the **???** with appropriate values, expressions or statements to ensure that the notebook runs properly end-to-end. 
# 
# Some things to keep in mind:
# 
# * Make sure to run all the code cells, otherwise you may get errors like `NameError` for undefined variables.
# * Do not change variable names, delete cells or disturb other existing code. It may cause problems during evaluation.
# * In some cases, you may need to add some code cells or new statements before or after the line of code containing the **???**. 
# * Since you'll be using a temporary online service for code execution, save your work by running `jovian.commit` at regular intervals.
# * Questions marked **(Optional)** will not be considered for evaluation, and can be skipped. They are for your learning.
# 
# You can make submissions on this page: https://jovian.ai/learn/data-analysis-with-python-zero-to-pandas/assignment/assignment-3-pandas-practice
# 
# If you are stuck, you can ask for help on the community forum: https://jovian.ai/forum/t/assignment-3-pandas-practice/11225/3. You can get help with errors or ask for hints, describe your approach in simple words, link to documentation, but **please don't ask for or share the full working answer code** on the forum.
# 
# 
# ## How to run the code and save your work
# 
# The recommended way to run this notebook is to click the "Run" button at the top of this page, and select "Run on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running Jupyter notebooks. 
# 
# Before starting the assignment, let's save a snapshot of the assignment to your Jovian.ai profile, so that you can access it later, and continue your work.

# In[1]:


import jovian


# In[2]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# In[3]:


# Run the next line to install Pandas
get_ipython().system('pip install pandas --upgrade')


# In[4]:


import pandas as pd


# In this assignment, we're going to analyze an operate on data from a CSV file. Let's begin by downloading the CSV file.

# In[5]:


from urllib.request import urlretrieve

urlretrieve('https://gist.githubusercontent.com/aakashns/28b2e504b3350afd9bdb157893f9725c/raw/994b65665757f4f8887db1c85986a897abb23d84/countries.csv', 
            'countries.csv')


# Let's load the data from the CSV file into a Pandas data frame.

# In[6]:


countries_df = pd.read_csv('countries.csv')


# In[7]:


countries_df


# **Q1: How many countries does the dataframe contain?**
# 
# Hint: Use the `.shape` method.

# In[8]:


num_countries = countries_df['location'].shape[0]


# In[9]:


print('There are {} countries in the dataset'.format(num_countries))


# In[10]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q2: Retrieve a list of continents from the dataframe?**
# 
# *Hint: Use the `.unique` method of a series.*

# In[11]:


continents = countries_df['continent'].unique()


# In[12]:


continents


# In[13]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q3: What is the total population of all the countries listed in this dataset?**

# In[14]:


total_population = countries_df['population'].sum()


# In[15]:


print('The total population is {}.'.format(int(total_population)))


# In[16]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: (Optional) What is the overall life expectancy across in the world?**
# 
# *Hint: You'll need to take a weighted average of life expectancy using populations as weights.*

# In[17]:


average_life_expectancy = countries_df.life_expectancy.mean()


# In[18]:


print('The average life expentacy is {}.'.format(int(average_life_expectancy)))


# In[19]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q4: Create a dataframe containing 10 countries with the highest population.**
# 
# *Hint: Chain the `sort_values` and `head` methods.*

# In[20]:


most_populous_df = countries_df.sort_values('population', ascending=False).head(10)


# In[21]:


most_populous_df


# In[22]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q5: Add a new column in `countries_df` to record the overall GDP per country (product of population & per capita GDP).**
# 
# 

# In[23]:


countries_df['gdp'] = countries_df['overall_gdp'] = countries_df['population']*countries_df['gdp_per_capita']


# In[24]:


countries_df


# In[25]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q: (Optional) Create a dataframe containing 10 countries with the lowest GDP per capita, among the counties with population greater than 100 million.**

# In[ ]:





# In[ ]:





# In[26]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q6: Create a data frame that counts the number countries in each continent**
# 
# *Hint: Use `groupby`, select the `location` column and aggregate using `count`.*

# In[27]:


country_counts_df = countries_df.groupby('continent')[['location']].count()


# In[28]:


country_counts_df


# In[29]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q7: Create a data frame showing the total population of each continent.**
# 
# *Hint: Use `groupby`, select the population column and aggregate using `sum`.*

# In[30]:


continent_populations_df = countries_df.groupby('continent')[['population']].sum()


# In[31]:


continent_populations_df


# In[33]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# Let's download another CSV file containing overall Covid-19 stats for various countries, and read the data into another Pandas data frame.

# In[34]:


urlretrieve('https://gist.githubusercontent.com/aakashns/b2a968a6cfd9fbbb0ff3d6bd0f26262b/raw/b115ed1dfa17f10fc88bf966236cd4d9032f1df8/covid-countries-data.csv', 
            'covid-countries-data.csv')


# In[35]:


covid_data_df = pd.read_csv('covid-countries-data.csv')


# In[36]:


covid_data_df


# **Q8: Count the number of countries for which the `total_tests` data is missing.**
# 
# *Hint: Use the `.isna` method.*

# In[77]:


total_tests_missing=pd.isna(covid_data_df.total_tests).sum()
 
total_tests_missing


# In[79]:


print("The data for total tests is missing for {} countries.".format(int(total_tests_missing)))


# In[80]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# Let's merge the two data frames, and compute some more metrics.
# 
# **Q9: Merge `countries_df` with `covid_data_df` on the `location` column.**
# 
# *Hint: Use the `.merge` method on `countries_df`.

# In[40]:


combined_df = countries_df.merge(covid_data_df, on="location")


# In[41]:


combined_df


# In[42]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q10: Add columns `tests_per_million`, `cases_per_million` and `deaths_per_million` into `combined_df`.**

# In[43]:


combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']


# In[44]:


combined_df['cases_per_million'] = combined_df['total_cases'] * 1e6 / combined_df['population']


# In[45]:


combined_df['deaths_per_million'] = combined_df['total_deaths'] * 1e6 / combined_df['population']


# In[46]:


combined_df


# In[47]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q11: Create a dataframe with 10 countires that have highest number of tests per million people.**

# In[48]:


highest_tests_df = combined_df.sort_values('tests_per_million',ascending=False).head(10)


# In[49]:


highest_tests_df


# In[50]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q12: Create a dataframe with 10 countires that have highest number of positive cases per million people.**

# In[51]:


highest_cases_df = combined_df.sort_values('cases_per_million',ascending=False).head(10)


# In[52]:


highest_cases_df


# In[53]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **Q13: Create a dataframe with 10 countires that have highest number of deaths cases per million people?**

# In[54]:


highest_deaths_df = combined_df.sort_values('deaths_per_million',ascending=False).head(10)


# In[55]:


highest_deaths_df


# In[56]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **(Optional) Q: Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".**

# In[57]:


highest_df = combined_df.sort_values(['tests_per_million', 'cases_per_million'], ascending=[False, False]).head(5)


# In[58]:


highest_df


# In[ ]:





# In[59]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# **(Optional) Q: Count number of countries that feature in both the lists "20 countries with lowest GDP per capita" and "20 countries with the lowest number of hospital beds per thousand population". Only consider countries with a population higher than 10 million while creating the list.**

# In[ ]:


lowest_gdp_df = combined_df[combined_df.population>10000000].sort_values('gdp_per_capita').head(20)


# In[ ]:


lowest_gdp_df


# In[60]:


lowest_beds_df = combined_df[combined_df.population>10000000].sort_values('hospital_beds_per_thousand').head(20)


# In[61]:


lowest_beds_df


# In[62]:


import jovian


# In[74]:


jovian.commit(project='pandas-practice-assignment', environment=None)


# ## Submission 
# 
# Congratulations on making it this far! You've reached the end of this assignment, and you just completed your first real-world data analysis problem. It's time to record one final version of your notebook for submission.
# 
# Make a submission here by filling the submission form: https://jovian.ai/learn/data-analysis-with-python-zero-to-pandas/assignment/assignment-3-pandas-practice
# 
# Also make sure to help others on the forum: https://jovian.ai/forum/t/assignment-3-pandas-practice/11225/2

# In[ ]:




