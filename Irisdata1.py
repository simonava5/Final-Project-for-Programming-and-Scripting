# Simona Vasiliauskaite
# 13/04/2018
# Calculating the mean of each column

# imported following modules and functions:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# I used pandas to load data from this file - iris.data.cs
data = pd.read_csv('irisdata.csv', header = 0)

print(data)

#calculate mean of sepal length

sepalength = data[:,0]
meansepalength = numpy.mean(data[:,0])
