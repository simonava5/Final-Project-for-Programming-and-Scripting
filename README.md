# Final-Project-for-Programming-and-Scripting
Final Project 2018 for Programming and Scripting module researching and analysing Fisher’s Iris data set.

## What does Iris Flower Data Set mean?

The Iris flower data set is a specific set of information compiled by Ronald Fisher, a biologist, in the 1930s. It describes particular biological characteristics of various types of Iris flowers, specifically, the length and width of both pedals and the sepals, which are part of the flower’s reproductive system. [Techopedia](https://www.techopedia.com/definition/32880/iris-flower-data-set)

## About Ronald Fisher

![Young Ronald Fisher](https://upload.wikimedia.org/wikipedia/commons/2/21/RonaldFisher1912.jpg)

Touted as the greatest scientist of his time, Sir Ronald Fisher (1890-1962) was a British statistician and biologist who was known for his contributions to experimental design and population genetics. 
For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics". In genetics, his work used mathematics to combine Mendelian genetics and natural selection; this contributed to the revival of Darwinism in the early 20th century revision of the theory of evolution known as the modern synthesis. Fisher also did experimental agricultural research, which has saved millions from starvation. [Wikipedia](https://en.wikipedia.org/wiki/Ronald_Fisher)

Before I started this project, I imported the following software libraries to analyze data. 

## What is Numpy?

Numpy provides functions for dealing with numerical data efficiently in Python. While Python does already provide good mathematical functionality out of the box, numpy is highly efficient at things like multiplying matrices and dealing with huge arrays of data. [Jupyter](https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#)

## What is Pandas?

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. [Pandas](https://pandas.pydata.org/)

Using pandas software library, open file irisdata.csv and analyse the data set.

First 5 rows of the data set:

sepal_length |  sepal_width | petal_length | petal_width |species
------------ | ------------ | ------------ | ----------- |-------
  5.1      |    3.5       |    1.4     |     0.2 | setosa
 4.9      |    3.0         |  1.4      |    0.2 | setosa
 4.7      |    3.2         | 1.3       |   0.2  | setosa
 4.6      |    3.1         |  1.5       |   0.2  | setosa
5.0      |    3.6         |  1.4      |    0.2 | setosa

Last 5 rows of the data set:

sepal_length | sepal_width | petal_length | petal_width  |  species
------------ | ----------- | ------------ | ------------ | ---------
6.7       |   3.0       |    5.2     |     2.3 |  virginica
6.3       |   2.5       |    5.0      |    1.9  | virginica
6.5       |   3.0       |    5.2      |    2.0  | virginica
6.2       |   3.4       |   5.4       |  2.3 |  virginica
5.9       |  3.0        |  5.1        |  1.8 |  virginica

Short statistical summary of Iris Data Set:

Description | sepal_length |    sepal_width |   petal_length |  petal_width
----------- |  ----------- |  ------------- |  ------------- |  -----------
count  |   150.000000  |  150.000000   |  150.000000  |   150.000000
mean   |     5.843333  |    3.054000   |    3.758667  |    1.198667
std    |     0.828066  |    0.433594   |    1.764420  |    0.763161
min    |     4.300000   |   2.000000   |   1.000000   |   0.100000
25%    |     5.100000  |    2.800000   |    1.600000  |    0.300000
50%    |     5.800000  |    3.000000   |    4.350000  |    1.300000
75%    |     6.400000  |    3.300000   |    5.100000  |    1.800000
max    |     7.900000  |    4.400000   |    6.900000  |    2.500000





REFERENCES:
1. https://en.wikipedia.org/wiki/Ronald_Fisher
2.  https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb
