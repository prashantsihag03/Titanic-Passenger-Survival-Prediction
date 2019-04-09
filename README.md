# Titanic-Passenger-Survival-Prediction
The analysis of what sorts of people were likely to survive in the popular titanic tragedy.

Using Machine learning tool - Logistic Regression for binary classification.

Data source: http://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html 

## Dependencies & Installation
Numpy https://pypi.org/project/numpy/

Matplotlib https://pypi.org/project/matplotlib/

Seaborn https://pypi.org/project/seaborn/

Pandas https://pypi.org/project/pandas/

## Dataset
The Dataset contains information about the passengers of the titanic.


## working 
*Checking the basic information about the dataset* <br>
dataset.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 887 entries, 0 to 886
Data columns (total 8 columns):
Survived    887 non-null int64
Pclass      887 non-null int64
Name        887 non-null object
Sex         887 non-null object
Age         887 non-null float64
SS          887 non-null int64
PC          887 non-null int64
Fare        887 non-null float64
dtypes: float64(2), int64(4), object(2)
memory usage: 55.5+ KB

*checking for null value*
dataset.isnull().sum()
Out[12]: 
Survived    0
Pclass      0
Name        0
Sex         0
Age         0
SS          0
PC          0
Fare        0
dtype: int64


*now, getting insights of the dataset by fetching few top records of dataset.*
dataset.head() 
Survived  Pclass   ...    PC     Fare
0         0       3   ...     0   7.2500
1         1       1   ...     0  71.2833
2         1       3   ...     0   7.9250
3         1       1   ...     0  53.1000
4         0       3   ...     0   8.0500



*Analyses dataset using graphs*

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/survived_graph.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/survival_wrt_gender.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/Survival_wrt_pclass.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/freq_wrt_age.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/freq_wrt_fare.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/count_wrt_ss.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/age_wrt_pclass.png)

