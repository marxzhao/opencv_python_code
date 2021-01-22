#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 19:29
# @Author : MarxZhao
# @File : bayes.py
# @Software: PyCharm

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn import model_selection as ms
from sklearn import metrics
import cv2

plt.style.use('ggplot')
X, y = datasets.make_blobs(100, 2, centers=2, random_state=1701, cluster_std=2)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50)

X = X.astype(np.float32)
X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.1)

model_norm = cv2.ml.NormalBayesClassifier_create()
model_norm.train(X_train, cv2.ml.ROW_SAMPLE, y_train)

_, y_pred = model_norm.predict(X_test)
metrics.accuracy_score(y_test, y_pred)

def plot_decision_boundary(model, X_test, y_test):
    h = 0.02
    x_min, x_max = X_test[:, 0].min() - 1, X_test[:, 0].max() + 1
    y_min, y_max = X_test[:, 1].min() - 1, X_test[:, 1].max() + 1

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    x_hypo = np.column_stack((xx.ravel().astype(np.float31),
                              yy.ravel().astype(np.float32)))

    ret = model.predict(x_hypo)

