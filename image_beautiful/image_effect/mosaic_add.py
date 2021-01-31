#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 14:29
# @Author : MarxZhao
# @File : mosaic_add.py
# @Software: PyCharm

from skimage import img_as_float
import matplotlib.pyplot as plt
from skimage import io
import random
import numpy as np
import cv2


def add_mosaic(image_name):
    img = io.imread(image_name)
    img = img_as_float(img)
    img_dst = img.copy()

    r, c, channel = img.shape
    half_path = 10      #马赛克大小
    for i in range(half_path, r - 1 - half_path, half_path):
        for j in range(half_path, c - 1 - half_path, half_path):
            k1 = random.random() - 0.5
            k2 = random.random() - 0.5
            m = np.floor(k1 * (half_path * 2 + 1))
            n = np.floor(k2 * (half_path * 2 + 1))
            h = int((i+m) % r)
            w = int((j+n) % c)
            img_dst[i - half_path:i + half_path, j - half_path:j + half_path, :] = img[h, w, :]

    return img_dst


if __name__=="__main__":

    image_name = '../data/1.jpg'
    image_dst = add_mosaic(image_name)
    cv2.imshow('dst', image_dst)
    cv2.waitKey(0)



