#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/24 11:08
# @Author : MarxZhao
# @File : kmeans_comp.py
# @Software: PyCharm


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.io import loadmat
#from skimage import io
from PIL import Image
from pylab import *
import k_means

def findClosestCentroids(X, centroids):  #之前定义的函数做一下修改，加上一个维度
    idx = []
    for i in range(len(X)):
        minus = X[i] - centroids
        dist = minus[:,0]**2 + minus[:,1]**2 +minus[:,2]**2  #加上minus[:,2]**2
        ci = np.argmin(dist)  #获取dist最小值的索引，即哪个中心离该样本最近
        idx.append(ci)
    return np.array(idx)


centroids = initCentroids(X, K)
idx, centroids_all = runKmeans(X, centroids, 10)


img = np.zeros(X.shape)
centroids = centroids_all[-1]
for i in range(len(centroids)):
    img[idx == i] = centroids[i]


img = img.reshape((128, 128, 3))
fig, axes = plt.subplots(1, 2, figsize=(12,6))
axes[0].imshow(A)
axes[1].imshow(img)
plt.show()
