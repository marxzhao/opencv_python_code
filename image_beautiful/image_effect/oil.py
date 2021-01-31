#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 14:18
# @Author : MarxZhao
# @File : oil.py
# @Software: PyCharm

import cv2
import numpy as np
import random
from PIL import Image
from PIL import ImageEnhance

def oil_style(image):
    h, w, n = image.shape
    dst = np.zeros((h-2, w, n), dtype='uint8')

    for i in range(1, h-2):
        for j in range(w -2):
            if random.randint(1, 10) % 3 == 0:
                dst[i, j] = image[i+1, j]
            elif random.randint(1, 10) % 2 == 0:
                dst[i, j] = image[i+2, j]
            else:
                dst[i, j] = image[i-1, j]

    return dst


def color_add_use_pil(image_name):
    image = Image.open(image_name)
    enh_oil = ImageEnhance.Color(image)
    color = 2.0
    image_colored = enh_oil.enhance(color)

    return image_colored


if __name__=="__main__":
    image_name = '../data/2.jpg'
    image = cv2.imread(image_name)
    dst = oil_style(image)

    cv2.imshow('one', dst)

    img_colored = color_add_use_pil(image_name)
    img_colored = np.asarray(img_colored)
    cv2.imshow('two', img_colored)
    cv2.waitKey(0)
