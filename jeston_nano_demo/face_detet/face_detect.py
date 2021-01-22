#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/22 21:52
# @Author : MarxZhao
# @File : face_detect.py.py
# @Software: PyCharm


import cv2
filepath = "test.jpeg" #用绝对路径
img = cv2.imread(filepath) # 读取图片
print(type(img))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转换灰色
print(type(gray))
# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier( "haarcascade_frontalface_default.xml" )
color = (0, 255, 0) # 定义绘制颜色
# 调用识别人脸
faceRects = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects): # 大于0则检测到人脸
    for faceRect in faceRects: # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
cv2.imshow("image", img) # 显示图像
c = cv2.waitKey(10)
cv2.waitKey(0)
cv2.destroyAllWindows()