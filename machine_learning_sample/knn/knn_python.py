#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/31 17:44
# @Author : MarxZhao
# @File : knn_python.py
# @Software: PyCharm

from sklearn.datasets._samples_generator import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
#生成已经标注的数据集
centers = [[-2, 2], [2, 2], [0, 4]]
X, y = make_blobs(n_samples=60, centers=centers,
                  random_state=0, cluster_std=0.60)

#显示数据
plt.figure(figsize=(16, 10), dpi=144)
c = np.array(centers)
plt.scatter(X[:,0], X[:,1], c=y, s=100, cmap='cool')
plt.scatter(c[:,0], c[:,1], s=100, marker='^', c='orange')


#KNN做分类
def use_for_classifier(k, X, y):
    #KNN分类
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X, y)


    #预测样本
    X_sample = [[0, 2]]
    y_sample = clf.predict(X_sample)
    print(y_sample)
    neighbors = clf.kneighbors(X_sample, return_distance=False)
    print(neighbors)

    #画图将预测点与其最近邻的K个点连起来
    plt.figure(figsize=(16, 10), dpi=144)
    plt.scatter(X[:,0], X[:,1], c=y, s=100, cmap='cool')
    plt.scatter(c[:,0], c[:,1], s=100, marker='^', c='k')
    plt.scatter(X_sample[0][0], X_sample[0][1], marker="x",
                c=y_sample, s=100, cmap='cool')
    for i in neighbors[0]:
        plt.plot([X[i][0], X_sample[0][0]], [X[i][1], X_sample[0][1]], 'k--', linewidth=0.6)

    plt.show()


#KNN做回归
def use_for_regressor(k):
    n_dots = 40
    X = 5 * np.random.rand(n_dots, 1)
    y = np.cos(X).ravel()
    y += 0.2 * np.random.rand(n_dots) - 0.1

    knn = KNeighborsRegressor(k)
    knn.fit(X, y)

    #回归方法：在X轴上的指定区间内生成足够多的点，针对这些足够密集的点，使用训练出来的模型进行预测
    #得到预测值y_pred，然后在坐标轴上，把所有的预测点连接起来，就画出了拟合曲线

    T = np.linspace(0, 5, 500)[:, np.newaxis]
    y_pred = knn.predict(T)
    #计算拟合后曲线针对训练样本的准确性
    knn.score(X, y)

    #将预测点连起来构成拟合曲线
    plt.figure(figsize=(16, 10), dpi=144)
    plt.scatter(X, y, c='g', label='data', s=100)
    plt.plot(T, y_pred, c='k', label='prediction', lw=4)
    plt.axis('tight')
    plt.title("KNeighborsRegressor (k=%i)" % k)
    plt.show()



if __name__=="__main__":
    k = 5
    use_for_regressor(k)