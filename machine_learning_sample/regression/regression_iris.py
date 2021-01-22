#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/3 23:01
# @Author : MarxZhao
# @File : regression_iris.py
# @Software: PyCharm

import numpy as np
import cv2
from sklearn import datasets
from sklearn import model_selection
from sklearn import metrics
import matplotlib.pyplot as plt
plt.style.use('ggplot')

iris = datasets.load_iris()
print(dir(iris))
print(iris.data.shape)
print(iris.target.shape)

idx = iris.target != 2
data = iris.data[idx].astype(np.float32)
target = iris.target[idx].astype(np.float32)

plt.scatter(data[:, 0], data[:, 1], c=target, cmap=plt.cm.Paired, s=100)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()

#拆分训练集测试集
X_train, X_test, y_train, y_test = model_selection.train_test_split(data, target, test_size=0.1, random_state=42)
print(X_train, X_test, y_train, y_test)

lr = cv2.ml.LogisticRegression_create()
lr.setTrainMethod(cv2.ml.LogisticRegression_MINI_BATCH)
lr.setMiniBatchSize(1)
lr.setIterations(100)

lr.train(X_train, cv2.ml.ROW_SAMPLE, y_train)
lr.get_learnt_thetas()

#测试分类器
ret, y_pred = lr.predict(X_train)
ms = metrics.accuracy_score(y_train, y_pred)
print('train :', ms)
ret, y_pred = lr.predict(X_test)
ms = metrics.accuracy_score(y_test, y_pred)
print('test :', ms)