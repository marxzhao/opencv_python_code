#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 18:45
# @Author : MarxZhao
# @File : svm.py
# @Software: PyCharm

#SVM 支持向量机 support vector machine

from sklearn import model_selection as ms
from sklearn import metrics

datadir = "data"
dataset = "pedestrains128x64"
datafile = "%s/%s.tar.gz" % (datadir, dataset)

extractdir = "%s/%s" % (datadir, dataset)

def extract_tar(filename):
    try:
        import tarfile
    except ImportError:
        raise  ImportError("You do not have tarfile installed. "
                           "Try unzipping the file outside of Python")

    tar = tarfile.open(datafile)
    tar.extractall(path=extractdir)
    tar.close()
    print("%s sucessfully extracted to %s" % (datafile, extractdir))

extract_tar(datafile)


import cv2
import matplotlib.pyplot as plt

for i in range(5):
    filename = "%s/per0010%d.ppm" % (extractdir, i)
    img = cv2.imread(filename)
    plt.subplot(1, 5, i + 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

#HOG 方向梯度直方图

win_size = (48, 96)
block_size = (16, 16)
block_stride = (8, 8)
cell_size = (8, 8)
num_bins = 9
hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, num_bins)

import numpy as np
import random
random.seed(42)

X_pos = []
for i in random.sample(range(900), 400):
    filename = "%s/per%05.ppm" % (extractdir, i)
    img = cv2.imread(filename)
    if img is None:
        print('Could not find image %s' % filename)
        continue
    X_pos.append(hog.compute(img, (64, 64)))

X_pos = np.array(X_pos, dtype=np.float32)
y_pos = np.ones(X_pos.shape[0], dtype=np.int32)
print(X_pos.shape, y_pos.shape)


def train_svm(X_train, y_train):
    svm = cv2.ml.SVM_create()
    svm.train(X_train, cv2.ml.ROW_SAMPLE, y_train)
    return svm

def score_svm(svm, X, y):
    _, y_pred = svm.predict(X)
    return metrics.accuracy_score(y, y_pred)

X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.2, random_state=42)

svm = train_svm(X_train, y_train)
score_svm(svm, X_train, y_train)


score_train = []
score_test = []
for j in range(3):
    svm = train_svm(X_train, y_train)
    score_train.append(score_svm(svm, X_train, y_train))
    score_test.append(score_svm(svm, X_test, y_test))

_, y_pred = svm.predict(X_test)
false_pos = np.logical_and((y_test.ravel() == -1), (y_pred.ravel() == 1))
if not np.any(false_pos):
    print(' no more false positives: done')
    break

X_train = np.concatenate((X_train, X_test[false_pos, :]), axis=0)
y_train = np.concatenate((y_train, y_test[false_pos]), axis=0)
