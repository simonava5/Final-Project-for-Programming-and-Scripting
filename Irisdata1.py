# Simona Vasiliauskaite
# 13/04/2018
# Final Project for Programming and Scripting
# Analysis of the Iris Data Set

# imported following modules and functions:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# use pandas to load data from this file - irisdata.csv
data = pd.read_csv('irisdata.csv', header = 0)

# check how many different types of species are in this data set

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

# use seaborn library to show the difference between all attributes
sns.boxplot(x='species', y='sepal_length', data=data)
sns.boxplot(x='species', y='sepal_width', data=data)
sns.boxplot(x='species', y='petal_length', data=data)
sns.boxplot(x='species', y='petal_width', data=data)
plt.show()

# show relationship between attributes using seaborn kdeplot
sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'petal_length') \
.add_legend()

sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'petal_width') \
.add_legend()

sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'sepal_length') \
.add_legend()

sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'sepal_width') \
.add_legend()

plt.show()

# separate each species values and compare each attribute
setosa = data[0:49]
versicolor = data[50:99]
virginica = data[100:149]

# to show the difference of all attributes I used a box and whisker plots
setosa.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
versicolor.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
virginica.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)

plt.show()