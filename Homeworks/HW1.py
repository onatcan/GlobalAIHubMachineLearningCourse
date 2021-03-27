#Explain your work

#Question 1

Machine learning is a branch of artificial intelligence (AI) that focuses on building applications that learn from data and improve accuracy over time without being programmed.
It focuses on applications that learn from experience and improve decision-making or predictive accuracy over time.

#Question 2

Supervised vs. Unsupervised Learning
- In a supervised learning model, the model can be trained using inputs and outputs, but outputs are not used to train the model in unsupervised learning.
- In supervised learning: Support vector machine, Neural network, Linear and logistics regression, random forest and classification trees algorithms;
  In unsupervised learning: algorithms such as Clustering, K-means, Hierarchical clustering, Association are used.
- Supervised learning is a simpler, more accurate and reliable method, while unsupervised learning is a numerically more complex and less reliable method.

#Question 3

– Training set: A set of examples used for learning, that is to fit the parameters of the classifier.
– Validation set: A set of examples used to tune the parameters of a classifier, for example to choose the number of hidden units in a neural network.
– Test set: A set of examples used only to assess the performance of a fully-specified classifier.
	
Validation set is different from test set. Validation set actually can be regarded as a part of training set, because it is used to build the model, neural networks or others. 
It is usually used for parameter selection and to avoild overfitting. If the model is non-linear (like NN) is trained on a training set only, it is very likely to get 100% accuracy and overfit, thus get very poor performance on test set. 
Thus a validation set, which is independant from the training set, is  used for parameter selection. In this process, people usually use "Cross Validation".
On the contrary, test test is only used to test the performance of a trained model. 

#Question 4

When it comes to creating a Machine Learning model, data preprocessing is the first step marking the initiation of the process. 
Typically, real-world data is incomplete, inconsistent, inaccurate (contains errors or outliers), and often lacks specific attribute values/trends. 
This is where data preprocessing enters the scenario – it helps to clean, format, and organize the raw data, thereby making it ready-to-go for Machine Learning models.

There are seven significant steps in data preprocessing in Machine Learning:
	
1. Removing Duplicate Values:
	
In most cases, the duplicates are removed so as to not give that particular data object an advantage or bias, when running machine learning algorithms.

2. Checking Imbalanced Data:
	
An Imbalanced dataset is one where the number of instances of a class(es) are significantly higher than another class(es), thus leading to an imbalance and creating rarer class(es).

3. Identifying and handling the missing values:
	
In data preprocessing, it is pivotal to identify and correctly handle the missing values, failing to do this, you might draw inaccurate and faulty conclusions and inferences from the data.
Basically, there are two ways to handle missing data:
	
	1- Deleting a particular row: In this method, you remove a specific row that has a null value for a feature or a particular column where more than 75% of the values are missing. 
However, this method is not 100% efficient, and it is recommended that you use it only when the dataset has adequate samples. 
You must ensure that after deleting the data, there remains no addition of bias. 

	2- Calculating the mean: This method is useful for features having numeric data like age, salary, year, etc. 
Here, you can calculate the mean, median, or mode of a particular feature or column or row that contains a missing value and replace the result for the missing value. 
This method can add variance to the dataset, and any loss of data can be efficiently negated. Hence, it yields better results compared to the first method (omission of rows/columns). 
Another way of approximation is through the deviation of neighbouring values. However, this works best for linear data.

4: Outlier Detection:
		
Outliers are extreme values that deviate from other observations on data , they may indicate a variability in a measurement, experimental errors or a novelty. 
In other words, an outlier is an observation that diverges from an overall pattern on a sample.
Some of the most popular methods for outlier detection are:
- Standart Deviation
- Box Plots / IQR Calculation
- Isolation Forest

5. Encoding the categorical data:
	
Categorical data refers to the information that has specific categories within the dataset. Machine Learning models are primarily based on mathematical equations. 
Thus, you can intuitively understand that keeping the categorical data in the equation will cause certain issues since you would only need numbers in the equations.

6. Splitting the dataset:
	
Every dataset for Machine Learning model must be split into two separate sets – training set and test set. 
Training set denotes the subset of a dataset that is used for training the machine learning model. Here, you are already aware of the output. 
A test set, on the other hand, is the subset of the dataset that is used for testing the machine learning model. The ML model uses the test set to predict outcomes.
Usually, the dataset is split into 70:30 ratio or 80:20 ratio. This means that you either take 70% or 80% of the data for training the model while leaving out the rest 30% or 20%. 
The splitting process varies according to the shape and size of the dataset in question. 

7. Feature scaling:
	
Feature scaling marks the end of the data preprocessing in Machine Learning. It is a method to standardize the independent variables of a dataset within a specific range. 
In other words, feature scaling limits the range of variables so that you can compare them on common grounds.
You can perform feature scaling in Machine Learning in two ways: Standardization and Normalization. 
Normalization typically means rescales the values into a range of [0,1]. 
Standardization typically means rescales data to have a mean of 0 and a standard deviation of 1 (unit variance).

#Question 5:

Discrete data is information that can only take certain values. These values don’t have to be whole numbers (a child might have a shoe size of 3.5 or a company may make a profit of £3456.25 for example) but they are fixed values – a child cannot have a shoe size of 3.72!
The number of each type of treatment a salon needs to schedule for the week, the number of children attending a nursery each day or the profit a business makes each month are all examples of discrete data. This type of data is often represented using tally charts, bar charts or pie charts.

Continuous data is data that can take any value. Height, weight, temperature and length are all examples of continuous data. Some continuous data will change over time; the weight of a baby in its first year or the temperature in a room throughout the day. 
This data is best shown on a line graph as this type of graph can show how the data changes over a given period of time. Other continuous data, such as the heights of a group of children on one particular day, is often grouped into categories to make it easier to interpret.

Discrete Variables and Probability Mass Functions

A probability distribution over discrete variables can be explained using a probability mass function (PMF). We typically express probability mass functions with a capital P. 
Usually, we associate each random variable with a different probability mass function, and the reader must determine which PMF to use based on the identity of the random variable instead of the name of the function; P (x) is generally not the same as P (y).

Continuous Variables and Probability Density Functions

When working with continuous random variables, we describe probability distributions using a probability density function (PDF) rather than a probability mass function. 

To analyze the given data we need to ask some questions like:
	
For Discrete Data Types:
- Can we estimate outcomes and probabilities,
- Is the data symmetric or asymmetric,
- Are the values clustered around a central value,
- Are the outliers positive or negative.

For Continous Data Types:
- Is the data symmetric or asymmetric,
- Is the data clustered around a central value,
- Where do the outliers lie, etc.

