#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 17:03
# @Author : MarxZhao
# @File : nmf.py
# @Software: PyCharm

#NMF 非负矩阵分解 Non-negative Matrix Factorization
from sklearn import decomposition

import numpy as np
import cv2
import matplotlib.pyplot as plt
plt.style.use('ggplot')

mean = [20, 20]
cov = [[5, 0], [25, 25]]
x, y = np.random.multivariate_normal(mean, cov, 1000).T

#show
plt.plot(x, y, 'o', zorder=1)
plt.axis([0, 40, 0, 40])
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()

#将特征向量组合成特征矩阵
X = np.vstack((x, y)).T

ica = decomposition.NMF()
X2 = ica.fit_transform(X)
plt.plot(X2[:, 0], X2[:, 1], 'o', zorder=1)
plt.xlabel('feature 1 pro comp')
plt.ylabel('feature 2 pro comp')
plt.show()