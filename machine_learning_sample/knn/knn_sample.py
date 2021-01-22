#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/3 16:34
# @Author : MarxZhao
# @File : knn_sample.py
# @Software: PyCharm

import numpy as np
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('ggplot')

single_data_point = np.random.randint(0, 100, 2)
single_label = np.random.randint(0, 2)

#数据生成
def generate_data(num_samples, num_features=2):
    data_size = (num_samples, num_features)
    data = np.random.randint(0, 100, size=data_size)
    labels_size = (num_samples, 1)
    labels = np.random.randint(0, 2, size=labels_size)

    return data.astype(np.float32), labels

def plot_data(all_blue, all_red):
    """
    :param all_blue:    所有蓝色数据
    :param all_red:     所有红色数据
    :return:
    """

    plt.scatter(all_blue[:, 0], all_blue[:, 1], c='b', marker='s', s=180)
    plt.scatter(all_red[:, 0], all_red[:, 1], c='r', marker='^', s=180)
    plt.xlabel('x coordinate (feature 1)')
    plt.ylabel('y coordinate (feature 2)')




if __name__=="__main__":
    #数据集生成
    num_samples = 12
    train_data, labels = generate_data(num_samples)
    print(train_data, labels)

    #数据显示
    blue = train_data[labels.ravel() == 0]
    red = train_data[labels.ravel() == 1]
    plot_data(blue, red)

    #训练分类器
    knn = cv2.ml.KNearest_create()
    knn.train(train_data, cv2.ml.ROW_SAMPLE, labels)

    #预测新数据
    newcomer, _ = generate_data(1)
    ret, results, neighbor, dist = knn.findNearest(newcomer, 2)
    print('newcomer:\t', newcomer)
    print("Predicted label:\t", results)
    print("Neighbor's label:\t", neighbor)
    print("Distance to neighbor:\t", dist)



