#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/3 16:08
# @Author : MarxZhao
# @File : base_dataset.py
# @Software: PyCharm

#常用数据集
"""
sklearn.dataset包
load_boston
load_iris
load_diabetes
load_digits
load_linnerud
fetch_olivetti_faces
fetch_20newsgroups

"""

from sklearn.datasets import fetch_openml
# dataset = fetch_openml('mnist_784')
# x, y = dataset["data"], dataset["target"]


#计算分类器精确率、准确率、召回率
from sklearn import metrics
# y_true = []
# y_pred = []
# metrics.accuracy_score(y_true, y_pred)
# metrics.precision_score(y_true, y_pred)
# metrics.recall_score(y_true, y_pred)

#计算回归器的均方误差、可释方差、R方值
import numpy as np

x = np.linspace(0, 10, 100)
y_true = np.sin(x) + np.random.rand(x.size) - 0.5
y_pred = np.sin(x)
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.plot(x, y_pred, linewidth=4, label='model')
plt.show()
mse = np.mean((y_true - y_pred) ** 2)
mse_p = metrics.mean_squared_error(y_true, y_pred)
print(mse, mse_p)

fvu = np.var(y_true - y_pred) / np.var(y_true)
fve = 1.0 - fvu

fve_p = metrics.explained_variance_score(y_true, y_pred)
print(fve, fve_p)

r2 = 1.0 - mse / np.var(y_true)
r2_p = metrics.r2_score(y_true, y_pred)
print(r2, r2_p)