# Final Project for Programming and Scripting 2018
Final Project 2018 for Programming and Scripting module researching and analysing Fisher’s Iris data set.

Project Objectives:

- [x] 1. Research background information about the data set and write a summary about it.
- [x] 2. Keep a list of references used in completing the project.
- [x] 3. Download the data set and write some Python code to investigate it.
- [x] 4. Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set.
- [x] 5. Write a summary of these investigations.
- [x] 6. Include supporting tables and graphics as you deem necessary.

# 1. RESEARCH

### Iris Flower Data Set

The Iris flower data set is a popular multivariate
dataset that was introduced by Ronald Fisher in 1930's. It reports on four different types of characteristics of three Iris Spieces - Iris Setosa, Iris Versicolor and Iris Virginica. It is widely used amongst programmers to practice different Python functions and run a series of methods to extract certain information. [1]

### About Ronald Fisher

![Young Ronald Fisher](https://upload.wikimedia.org/wikipedia/commons/2/21/RonaldFisher1912.jpg)

Known as the greatest scientist of his time, Ronald Fisher was a British statistician and biologist who was known for his contributions to experimental design and population genetics. 

He has been described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics". Fisher also did experimental agricultural research, which has saved millions from starvation. 
Ronald Fisher introduced the Iris Data Set but it was Edgar Anderson who actually collected the data. [2]

### Instructions

In order to successfully run this code you first must install the following software:

1. [Python](https://www.python.org/downloads/) via Anaconda3
2. [Visual Studio Code](https://code.visualstudio.com/)

Also import the following software libraries in visual code where you are going to run this code: 

1. Numpy [import *numpy* as *np*]
2. Pandas [import *pandas* as *pd*]
3. Matplotlib [import *matplotlib.pyplot* as *plt*]
4. Seaborn [import *seaborn* as *sns*]

Save the data set from this [link](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
or use it from my GitHub account [here](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/irisdata.csv), click raw to copy and save it on your device. 

You can find the code I created to analyse this dataset in **Irisdata1.py** file.

Using pandas software library, open file irisdata.csv

```Data = pd.read_csv('irisdata.csv', header = 0)```

-----------------------------------------------------------------------------------------------------------------------

About the libraries which I will be using for this analysis:

### What is Numpy?

Numpy provides functions for dealing with numerical data efficiently in Python. Numpy is highly efficient at things like multiplying matrices and dealing with huge arrays of data. [3]

### What is Pandas?

Pandas is an open source, BSD-licensed library that provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. [4]

### What is Matplot?

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.[5]

### What is Seaborn?

Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.[6]

# 2. ANALYSIS

In this analysis of the Iris Data Set, I will be looking at 3 species - Iris Setosa, Iris Virginica, Iris Versicolor and their four variables in cm. These are as follows:

* Sepal Lenght
* Sepal Width
* Petal Length
* Petal Width

![Iris Flower](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Iris%20flower%20petal%20and%20sepal.jpg)

**Line 17**

Check for the amount of each species in this data set

``print(data["species"].value_counts())``

*Output:*

versicolor    50
virginica     50
setosa        50

**Line 21 and 24**

Before diving deep into this data set, I quickly pulled up first and last 5 rows of the data to check that everything looks correct and that it matches the csv file I imported with the Iris Data Set.

`data.head(5)`

First 5 rows of the data set:

 **TABLE 1.**

sepal_length |  sepal_width | petal_length | petal_width |species
------------ | ------------ | ------------ | ----------- |-------
  5.1      |    3.5       |    1.4     |     0.2 | setosa
 4.9      |    3.0         |  1.4      |    0.2 | setosa
 4.7      |    3.2         | 1.3       |   0.2  | setosa
 4.6      |    3.1         |  1.5       |   0.2  | setosa
5.0      |    3.6         |  1.4      |    0.2 | setosa

`data.tail(5)`

Last 5 rows of the data set:

 **TABLE 2.**

sepal_length | sepal_width | petal_length | petal_width  |  species
------------ | ----------- | ------------ | ------------ | ---------
6.7       |   3.0       |    5.2     |     2.3 |  virginica
6.3       |   2.5       |    5.0      |    1.9  | virginica
6.5       |   3.0       |    5.2      |    2.0  | virginica
6.2       |   3.4       |   5.4       |  2.3 |  virginica
5.9       |  3.0        |  5.1        |  1.8 |  virginica

**Line 27**

For a statistical summary of the data set including the count, mean, standard deviation and percentiles of each column, I used following code:

`data.describe()`

Short statistical summary of Iris Data Set:

 **TABLE 3.**

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


We can see from this table that the average length and width of a sepal is **5.8** and **3.05**
and the average length and width of a petal is **3.75** and **1.19** indicating that a petal of the Iris spieces is smaller in size than the sepal.

**Line 30-31**

I used this code to get an overall view at the data set using a histogram.

`data.hist()`
`plt.show()`

 **HISTOGRAM 1.**

![Figure 1. Distribution of input attribute](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Figure%201.%20Distribution%20of%20input%20attributes.png)

**Line 34-35**

Using subplots, I compared each variable on a different axis with the following code:

`data.plot(subplots=True, figsize=(6, 6))
plt.show()`

 **DIAGRAM 1.**

![Figure 2. Showing variables on different axis](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Figure%202.%20Differences%20between%20each%20variable.png)

We can clearly see by this diagram that petal length and width are the smallest from 0-50 and increase in size again from 50-100 and again from 100-150. As we already know from our data that rows 0-50 represent Iris Setosa, 50-100 - Iris Versicolor and 100-150 Iris Virginica, so it is undeniable that Iris Setosa have the smallest petals and Iris Virginica have the largest. 

**Lines 38-42**

I also discovered another great way to visualise this data is through seaborn library. These plots provide a very clear relationship between the variables of each species. This version is much clearer and crisp then the subplots I used on lines 44.

`sns.boxplot(x='species', y='sepal_length', data=data)
sns.boxplot(x='species', y='sepal_width', data=data)
sns.boxplot(x='species', y='petal_length', data=data)
sns.boxplot(x='species', y='petal_width', data=data)`

**DIAGRAM 2.**

![Relationship between spieces variables - sepal length and width](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Sepal%20Width%20%26%20Length.png)

![Relationship between spieces variables - petal length and width](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Petal%20Width%20%26%20Length.jpg)

**Line 45-62**

To visualise this data's attributes on a curve diagram, I used another function from seaborn library

`sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'petal_length') \
.add_legend()`

`sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'petal_width') \
.add_legend()`

`sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'sepal_length') \
.add_legend()`

`sns.FacetGrid(data, hue='species', size=6) \
.map(sns.kdeplot, 'sepal_width') \
.add_legend()`

**DIAGRAM 3.**

![Petal Length](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Curve%20Diagram%20Petal%20L.png)

![Petal Width](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Curve%20Diagram%20Petal%20W.png)

![Sepal Length](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Curve%20Diagram%20Sepal%20L.png)

![Sepal Width](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/Curve%20Diagram%20Sepal%20W.png)

It's very clear from these diagrams how much they differ in size.

**Line 64-71**

To show the difference between each species attributes I sliced the values into three groups and produced box and whisker plots. As I mentioned above I found boxplots to represent this data better, but I will leave this code below.

`setosa = data[0:49]`
`versicolor = data[50:99]`
`virginica = data[100:149]`

`setosa.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)`

`versicolor.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)`

`virginica.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)`

**DIAGRAM 4.**

![Iris Setosa](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/setosa.png)

![Iris Versicolor](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/versicolor.png)

![Iris Virginica](https://github.com/simonava5/Final-Project-for-Programming-and-Scripting/blob/master/virginica.png)

This diagram provides us with a clear visualization of each species variables. The biggest difference can be seen between Iris Setosa and Iris Virginica, and Iris Versicolor falls somewhere in the middle.

# 3. CONCLUSION

I found it extremely useful to get a general idea about the data to begin with using simple Python functions such as **describe()**. It provided me with some basic information which gave me a greater understanding of what I've to work with.

We can see from **Table 3** that the average length and width of a sepal is 5.8 and 3.05, and the average length and width of a petal is 3.75 and 1.19 indicating that a petal of the Iris spieces is smaller in size than the sepal.

We can clearly see from **Diagram 1** that petal length and width are the smallest from 0-50 and increase in size again from 50-100 and again from 100-150. As we already know from our data that rows 0-50 represent Iris Setosa, 50-100 - Iris Versicolor and 100-150 Iris Virginica, so it is undeniable that Iris Setosa have the smallest petals and Iris Virginica have the largest. 

Again in **Diagram 2** shows a very distinctive size difference in each species with Iris Virginica proving to be the largest.

**Diagram 4** provides us with a clear visualization of each species variables. The biggest difference can be seen between Iris Setosa and Iris Virginica, and Iris Versicolor falls somewhere in the middle.

Over all, visualisating the data using **Matplotlib** gave me a great insight of how data can be represented. It clearly demonstrated the different patterns and relationships between the variables. It gives data a totally different dynamic. After further research into the different libraries available for **data representation** I did find seaborn to be useful too. 

--------------------------------------------------------------------------------
### REFERENCES:
1. http://patrickhoey.com/downloads/Computer_Science
2. https://en.wikipedia.org/wiki/Ronald_Fisher
3. http://www.numpy.org/
4. https://pandas.pydata.org/ 
5. https://matplotlib.org/
6. https://seaborn.pydata.org/
7. https://archive.ics.uci.edu/ml/datasets/Iris
