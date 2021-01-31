#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 14:00
# @Author : MarxZhao
# @File : retro_style.py
# @Software: PyCharm

import cv2
import numpy as np

def retro_style(image):
    h, w, n = image.shape
    image_dst = image.copy()
    for i in range(h):
        for j in range(w):
            b = image[i, j][0]
            g = image[i, j][1]
            r = image[i, j][2]
            B = int(0.272 * r + 0.534 * g + 0.131 * b)
            G = int(0.349 * r + 0.686 * g + 0.168 * b)
            R = int(0.393 * r + 0.769 * g + 0.189 * b)
            image_dst[i, j][0] = max(0, min(B, 255))
            image_dst[i, j][1] = max(0, min(G, 255))
            image_dst[i, j][2] = max(0, min(R, 255))

    return image_dst


if __name__=="__main__":
    image = cv2.imread('../data/1.jpg')
    image_dst = retro_style(image)
    cv2.imshow('dst', image_dst)
    cv2.waitKey(0)