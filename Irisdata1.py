# Simona Vasiliauskaite
# 13/04/2018
# Final Project for Programming and Scripting
# Analysis of the Iris Data Set

# imported following modules and functions:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# I used pandas to load data from this file - iris.data.cs
data = pd.read_csv('irisdata.csv', header = 0)

# Before analysing the data set, I 

# quick analysis of the data
# checking first 10 rows of the data
data.head(10)

# checking last 10 rows of the data
data.tail(10)

# checking statistical summary of the data set
data.describe()

# add a histogram to visualise data set

data.hist()
plt.show()

# using subplots, add a histogram of each variable on a different axis

data.plot(subplots=True, figsize=(6, 6))
plt.show()

# I wanted to use diagrams that make sense for this data analysis and this pie chart
# incidates the density of each variable.

series = pd.Series(3 * np.random.rand(4), index=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
series.plot.pie(figsize=(6, 6))
plt.show()



data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()








