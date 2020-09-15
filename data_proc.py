# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset from datasheet
dataset = pd.read_csv ('Data.csv')
#all but the last column :-1
X= dataset.iloc[:,:-1].values
y= dataset.iloc[:,3].values 

#missing data management
#from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')

#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis =0)
imputer = imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform (X[:,1:3])

#Encoding categorical values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
LabelEncoder_X = LabelEncoder()
X[:, 0] = LabelEncoder_X.fit_transform(X[:, 0])

columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])],     
                                      remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X),dtype=np.str)

LabelEncoder_y = LabelEncoder()
y = LabelEncoder_y.fit_transform(y)
# columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [3])],     
#                                       remainder='passthrough')
# y=np.array(columnTransformer.fit_transform(y),dtype=np.str)

#Splitting datasets into test and training sets nb train sz + tst sz = 1
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.2, random_state=0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

