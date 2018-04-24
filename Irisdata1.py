# Simona Vasiliauskaite
# 13/04/2018
# Final Project for Programming and Scripting
# Analysis of the Iris Data Set

# imported following modules and functions:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# I used pandas to load data from this file - iris.data.csv
data = pd.read_csv('irisdata.csv', header = 0)

# to check that there is definately three different spieces
# investigated

print(data['species'].value_counts())

# quick analysis of the data
# checking first 5 rows of the data
print(data.head(5))

# check last 5 rows of the data
print(data.tail(5))

# check statistical summary of the data set
print(data.describe())

# add a histogram to visualise data set

data.hist()
plt.show()

# using subplots, add a histogram of each variable on a different axis

data.plot(subplots=True, figsize=(6, 6))
plt.show()

# using seaborn library to show the difference for each variable
# in each species

sns.boxplot(x='species', y='sepal_length', data=data)
sns.boxplot(x='species', y='sepal_width', data=data)
sns.boxplot(x='species', y='petal_length', data=data)
sns.boxplot(x='species', y='petal_width', data=data)


# I wanted to use diagrams that make sense for this data analysis and this pie chart
# incidates the density of each variable.

series = pd.Series(3 * np.random.rand(4), index=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
series.plot.pie(figsize=(6, 6))
plt.show()

# Separate each species values and compare each attribute

setosa = data[0:49]
versicolor = data[50:99]
virginica = data[100:149]

# to show the difference in each species attributes I used a box and whisker plots

setosa.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
versicolor.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
virginica.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)










