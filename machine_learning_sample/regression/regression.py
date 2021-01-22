#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/3 22:39
# @Author : MarxZhao
# @File : regression.py
# @Software: PyCharm

#KNN回归模型

import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn import model_selection as modsel
from sklearn import linear_model
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#载入数据集
boston = datasets.load_boston()
print(dir(boston))
print(boston.data.shape)
print(boston.target.shape)

#载入iris数据集
iris = datasets.load_iris()
idx = iris.target != 2
data = iris.data[idx].astype(np.float32)
target = iris.target[idx].astype(np.float32)


#训练模型
linreg = linear_model.LinearRegression()
X_train, X_test, y_train, y_test = modsel.train_test_split(
    boston.data, boston.target, test_size=0.1,
    random_state=42)
linreg.fit(X_train, y_train)
linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
metrics.mean_squared_error(y_train, linreg.predict(X_train))
linreg.score(X_train, y_train)
print(1)
#测试模型
y_pred = linreg.predict(X_test)
metrics.mean_squared_error(y_test, y_pred)

plt.figure(figsize=(10, 6))
plt.plot(y_test, linewidth=3, label='ground truth')
plt.plot(y_pred, linewidth=3, label='predicted')
plt.legend(loc='best')
plt.xlabel('test_data points')
plt.ylabel('target value')

plt.plot(y_test, y_pred, 'o')
plt.plot([-10, 60], [-10, 60], 'k--')
plt.axis([-10, 60, -10, 60])
plt.xlabel('ground truth')
plt.ylabel('predicted')

scorestr = r'R$^2$ = %.3f' % linreg.score(X_test, y_test)
errstr = 'MSE = %.3f' % metrics.mean_squared_error(y_test, y_pred)
plt.text(-5, 50, scorestr, fontsize=12)
plt.text(-5, 45, errstr, fontsize=12)

plt.show()


