#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 13:38
# @Author : MarxZhao
# @File : haha.py
# @Software: PyCharm

import cv2
import math
import numpy as np

def max_frame(image, radius, cx, cy):
    h, w, n = image.shape

    real_radius = int(radius / 2.0)
    image_dst = image.copy()

    for i in range(w):
        for j in range(h):
            tx = i - cx
            ty = j - cy
            distance = tx * tx + ty * ty
            if distance < radius * radius:
                nx = int(tx / 2.0)
                ny = int(ty / 2.0)
                nx = int(nx * (math.sqrt(distance) / real_radius))
                ny = int(ny * (math.sqrt(distance) / real_radius))
                nx = int(nx + cx)
                ny = int(ny + cy)
                if nx < w and ny < h:
                    image_dst[j, i][0] = image[ny, nx][0]
                    image_dst[j, i][1] = image[ny, nx][1]
                    image_dst[j, i][2] = image[ny, nx][2]

    return image_dst


def min_frame(image, radius, cx, cy):
    h, w, n = image.shape
    image_dst = image.copy()

    for i in range(w):
        for j in range(h):
            tx = i - cx
            ty = j - cy
            theta = math.atan2(ty, tx)
            distance = math.sqrt((tx * tx) + (ty * ty))
            nx = int(cx + (math.sqrt(distance) * radius * math.cos(theta)))
            ny = int(cy + (math.sqrt(distance) * radius * math.sin(theta)))
            if 0 < nx < w and 0 < ny < h:
                image_dst[j, i][0] = image[ny, nx][0]
                image_dst[j, i][1] = image[ny, nx][1]
                image_dst[j, i][2] = image[ny, nx][2]
    return image_dst


if __name__=="__main__":
    image = cv2.imread('../data/1.jpg', -1)
    print(image.shape)
    h, w = image.shape[:2]
    print(h, w)
    ch, cw = int(h/2), int(w/2)
    img_max = max_frame(image, 150, cw, ch)
    img_min = min_frame(image, 12, cw, ch)
    cv2.imshow('src', image)
    cv2.imshow('max', img_max)
    cv2.imshow('min', img_min)

    cv2.waitKey(0)
