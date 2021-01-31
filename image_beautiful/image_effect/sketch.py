#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 14:05
# @Author : MarxZhao
# @File : sketch.py
# @Software: PyCharm

import cv2
import numpy as np


def edge_filter(image):
    img_tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_tmp = cv2.medianBlur(img_tmp, 7)
    img_tmp = cv2.Laplacian(img_tmp, cv2.CV_8U, 5)
    ret, thresh = cv2.threshold(img_tmp, 127, 255, cv2.THRESH_BINARY_INV)

    return thresh

def sketch_style(image):
    h, w, n = image.shape
    gray_zero = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_tmp = np.zeros((h, w), dtype='uint8')
    gray_one = cv2.addWeighted(gray_zero, -1, img_tmp, 0, 255, 0)

    gray_one = cv2.GaussianBlur(gray_one, (11, 11), 0)
    dst = cv2.addWeighted(gray_zero, 0.5, gray_one, 0.5, 0)
    return dst

if __name__=="__main__":
    image = cv2.imread('../data/1.jpg')
    image_dst = sketch_style(image)
    cv2.imshow('dst', image_dst)
    cv2.waitKey(0)