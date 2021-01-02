#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/2 19:24
# @Author : MarxZhao
# @File : utils.py
# @Software: PyCharm

import cv2
import os
import numpy as np

def is_file_exist(path):
    return os.path.exists(path)

def cvmat_to_string(img):
    img_encode = cv2.imencode('.jpg', img)[1]
    data_encode = np.array(img_encode)
    str_encode = data_encode.tostring()

    return str_encode

def string_to_cvmat(imagebuf, mode="webp"):
    nparr = np.fromstring(imagebuf, np.uint8)
    if mode in ["webp"]:
        img = cv2.imdecode(nparr, 1)
    else:
        img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    img = png_processing(img)

    return img



class ConfigDict(dict):
    def __init__(self, origin_dict, **kw):
        super(ConfigDict, self).__init__(**kw)
        for key in origin_dict:
            self[key] = origin_dict[key]

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'config' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value



def png_processing(img):
    if len(img.shape) < 3:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:
        img = img.astype(np.float)
        img = img / 255
        img1, img2, img3, img4 = cv2.split(img)
        bg = np.ones((img.shape[0], img.shape[1]), dtype=np.float)
        img1 = bg * (1 - img4) + img1 * img4
        img2 = bg * (1 - img4) + img2 * img4
        img3 = bg * (1 - img4) + img3 * img4
        img = cv2.merge([img1, img2, img3]) * 255

    return img.astype(np.uint8)