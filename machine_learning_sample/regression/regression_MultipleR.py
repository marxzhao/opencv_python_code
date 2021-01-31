#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/31 16:32
# @Author : MarxZhao
# @File : regression_MultipleR.py
# @Software: PyCharm


import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import metrics
from sklearn import model_selection as modsel
from sklearn import linear_model
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn

#载入数据集
boston_data = datasets.load_boston()
# print(boston_data.keys())
# print(boston_data.DESCR)

boston_data_frame = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
#检查丢失的信息
print(boston_data_frame.isnull().sum())

#分离自变量和因变量
boston_data_x = boston_data_frame[boston_data_frame.columns[0:13]]
boston_data_y = boston_data_frame[boston_data_frame.columns[13:14]]
#检查相关性
print(boston_data_x.corr())
#利用heatmap可视化属性之间的相关性
seaborn.heatmap(boston_data_x.corr())

#创建相关矩阵
abs_corr_matrix = boston_data_x.corr().abs()
up_tri = abs_corr_matrix.where(np.triu(np.ones(abs_corr_matrix.shape), k=1).astype(np.bool))

correlated_features = [col for col in up_tri.columns if any(up_tri[col] > 0.75)]
#输出相关性
print(correlated_features)

#降低相关性

boston_data_x = boston_data_x.drop(correlated_features, axis=1)
X_train, X_test, Y_train, Y_test = modsel.train_test_split(boston_data_x, boston_data_y, test_size=0.20)

print(len(X_train), len(Y_train), len(X_test), len(Y_test))
#创建多元线性回归对象
linear_regression = linear_model.LinearRegression()
linear_regression.fit(X_train, Y_train)

Y_pred = linear_regression.predict(X_test)
#均方误差
print("Mean squared error: %.1f" % metrics.mean_squared_error(Y_test, Y_pred))
#R^2系数
print("R2 Score: %.2f" % metrics.r2_score(Y_test, Y_pred))
#平均绝对误差
print("Mean absolute error: %.2f" % metrics.mean_absolute_error(Y_test, Y_pred))



#使用K交叉验证来计算误差
kfold = modsel.KFold(len(boston_data_frame), n_folds=10, shuffle=True)
mean_abs_errors = list()
for train, test in kfold:
    linear_regression.fit(boston_data_x.ix[train], boston_data_y.ix[train])
    Y_test = boston_data_y.ix[test]
    Y_pred = linear_regression.predict(boston_data_x.ix[test])
    mean_abs_errors.append(metrics.mean_absolute_error(Y_test, Y_pred))

print('10 Fold Cross validation Error', np.mean(mean_abs_errors))