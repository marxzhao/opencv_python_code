#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 14:43
# @Author : MarxZhao
# @File : catoon.py
# @Software: PyCharm

import cv2
import numpy as np

def catoon_style(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.blur(gray, (7, 7))
    edge = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)
    catoon = cv2.bitwise_and(image, edge)

    return catoon

if __name__=="__main__":
    image_name = '../data/1.jpg'
    image = cv2.imread(image_name)
    image_dst = catoon_style(image)
    cv2.imshow('dst', image_dst)
    cv2.waitKey(0)
