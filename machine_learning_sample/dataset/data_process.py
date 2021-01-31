#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 14:23
# @Author : MarxZhao
# @File : data_process.py
# @Software: PyCharm



#特征标准化

from sklearn import preprocessing
import numpy as np

X = np.array([[1, 2, 3], [3, 0, -1], [0, 1, -1]])
X_scaled = preprocessing.scale(X)
print(X_scaled)
print(X_scaled.mean(axis=0))
print(X_scaled.std(axis=0))

#特征归一化
X_norm_l1 = preprocessing.normalize(X, norm='l1')
print(X_norm_l1)
X_norm_l2 = preprocessing.normalize(X, norm='l2')
print(X_norm_l2)

#特征缩放,默认缩放到0-1
min_max_scaler = preprocessing.MinMaxScaler()
X_min_max = min_max_scaler.fit_transform(X)
print(X_min_max)
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-10, 10))
print(min_max_scaler.fit_transform(X))

#二值特征化
binarizer = preprocessing.Binarizer(threshold=0.5)
X_binarizer = binarizer.transform(X)
print(X_binarizer)

#确实数据处理
from numpy import nan
from sklearn.impute import SimpleImputer
X = np.array([[nan, 0, ],
              [2, 9, -8],
              [1, nan, 1],
              [5, 2, 4],
              [7, 6, -3]])
imp = SimpleImputer(strategy='median')  #mean，median，most_frequent，constant
X2 = imp.fit(X)
print(X2)



data = [
    {'name': 'dasda', 'born': 1912, 'died': 2014},
    {'name': 'sd', 'born': 1952, 'died': 1994},
    {'name': 'cc', 'born': 1925, 'died': 1984},
    {'name': 'hgn', 'born': 1976, 'died': 1990}
]

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False, dtype=int)
X2 = vec.fit_transform(data)
print(X2)
