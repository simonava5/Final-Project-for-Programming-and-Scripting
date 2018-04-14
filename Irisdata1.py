# Simona Vasiliauskaite
# 13/04/2018
# Calculating the mean of each column

# imported following modules and functions:
import numpy
import matplotlib.pyplot as plt
import pandas


#used this function to open iris.data.csv which is saved on my device and separate all values with a coma delimiter
data = numpy.genfromtxt('iris.data.csv', delimiter=',')

#listing all data from the first column of the data set which is the sepal length 
firstcol = data[:,0]

#listing all the data from the second column of the data set which is the sepal width
secondcol = data[:, 1]



