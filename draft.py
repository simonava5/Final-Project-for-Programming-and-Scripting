
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# I used pandas to load data from this file - iris.data.cs
data = pd.read_csv('irisdata.csv', header = 0)

# quick analysis of the data
# checking first 5 rows of the data
print(data.head(5))

# check last 5 rows of the data
print(data.tail(5))