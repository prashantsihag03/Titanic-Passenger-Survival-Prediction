# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:34:26 2018

@author: Prashant
"""

import numpy as np
import matplotlib as plt
import seaborn as sns
import pandas as pd

#Load dataset
dataset = pd.read_csv('titanic.csv')
dataset.head(5)

#Analysing dataset
Survival = sns.countplot(x="Survived", data=dataset)
Survival_wrt_sex = sns.countplot(x="Survived", hue="Sex", data=dataset)
Survival_wrt_pclass = sns.countplot(x="Survived", hue="Pclass", data=dataset)
dataset["Age"].plot.hist()
dataset["Fare"].plot.hist(bin=20, figsize=(10,5))
dataset.info()
sns.countplot(x="SS", data=dataset)
sns.boxplot(x="Pclass", y="Age", data=dataset)

#Null valve check
dataset.isnull().sum()

#data preparation
dataset.drop("Name", axis=1, inplace=True)
dataset.head(10)

sex = pd.get_dummies(dataset['Sex'],drop_first=True)
pcl = pd.get_dummies(dataset['Pclass'],drop_first=True)
dataset= pd.concat([dataset, sex, pcl], axis=1)
dataset.head(5)
dataset.drop(["Sex","Pclass"], axis=1, inplace=True)


#Train Data
X=dataset.drop("Survived", axis=1)
y=dataset["Survived"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#building classifier
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

prediction= classifier.predict(X_test)

#prediction reports and accuracy
from sklearn.metrics import classification_report
classification_report(y_test,prediction)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,prediction)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,prediction)
