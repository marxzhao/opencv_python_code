#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 14:40
# @Author : MarxZhao
# @File : pca.py
# @Software: PyCharm

#PCA 主成分分析 Principal Component Analysis

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
mu, eig = cv2.PCACompute(X, np.array([]))
print(eig)
print(mu)

# plt.plot(x, y, 'o', zorder=1)
# plt.quiver(mu[0][0], mu[0][1], eig[:, 0], eig[:, 1], zorder=3, scale=0.2, units='xy')
# plt.text(mu[0][0] + 5 * eig[0, 0], mu[0][1] + 5 * eig[0, 1], 'u1', zprder=5, fontsize=16,
#          bbox=dict(facecolor='white', alpha=0.6))
# plt.text(mu[0][0] + 7 * eig[1, 0], mu[0][1] + 4 * eig[1, 1], 'u1', zprder=5, fontsize=16,
#          bbox=dict(facecolor='white', alpha=0.6))
# plt.axis([0, 40, 0, 40])
# plt.xlabel('feature 1')
# plt.ylabel('feature 2')
# plt.show()

#使用PCAProject旋转数据
X2 = cv2.PCAProject(X, mu, eig)
plt.plot(X2[:, 0], X2[:, 1], 'o', zorder=1)
plt.xlabel('feature 1 pro comp')
plt.ylabel('feature 2 pro comp')
plt.show()