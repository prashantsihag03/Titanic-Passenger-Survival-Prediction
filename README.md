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
**Checking the basic information about the dataset** <br>
dataset.info()<br>
<class 'pandas.core.frame.DataFrame'><br>
RangeIndex: 887 entries, 0 to 886<br>
Data columns (total 8 columns):<br>
Survived    887 non-null int64<br>
Pclass      887 non-null int64<br>
Name        887 non-null object<br>
Sex         887 non-null object<br>
Age         887 non-null float64<br>
SS          887 non-null int64<br>
PC          887 non-null int64<br>
Fare        887 non-null float64<br>
dtypes: float64(2), int64(4), object(2)<br>
memory usage: 55.5+ KB<br>

**checking for null value**<br>
dataset.isnull().sum()<br>
Out[12]: <br>
Survived    0<br>
Pclass      0<br>
Name        0<br>
Sex         0<br>
Age         0<br>
SS          0<br>
PC          0<br>
Fare        0<br>
dtype: int64<br>


**now, getting insights of the dataset by fetching few top records of dataset.**<br>
dataset.head() <br>
Survived  Pclass   ...    PC     Fare<br>
0         0       3   ...     0   7.2500<br>
1         1       1   ...     0  71.2833<br>
2         1       3   ...     0   7.9250<br>
3         1       1   ...     0  53.1000<br>
4         0       3   ...     0   8.0500<br>



**Analyses dataset using graphs**

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/survived_graph.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/survival_wrt_gender.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/Survival_wrt_pclass.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/freq_wrt_age.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/freq_wrt_fare.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/count_wrt_ss.png)

![Image of bar graph](https://github.com/prashantsihag03/Titanic-Passenger-Survival-Prediction/blob/master/graphs/age_wrt_pclass.png)

