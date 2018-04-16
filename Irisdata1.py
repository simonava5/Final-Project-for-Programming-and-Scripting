# Simona Vasiliauskaite
# 13/04/2018
# Calculating the mean of each column

# imported following modules and functions:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# I used pandas to load data from this file - iris.data.cs
data = pd.read_csv('irisdata.csv', header = 0)

# quick analysis of the data
# checking first 10 rows of the data
data.head()

# checking last 10 rows of the data
data.tail()

# checking statistical summary of the data set
data.describe()

