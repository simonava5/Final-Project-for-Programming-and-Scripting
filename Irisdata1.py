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



