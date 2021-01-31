#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 16:15
# @Author : MarxZhao
# @File : video_shake.py
# @Software: PyCharm

import cv2
import numpy as np



def video_shake_image(image):
    h, w, c = image.shape
    ha = int(h * 0.1)
    hb = int(h * 0.9)
    wa = int(w * 0.1)
    wb = int(w * 0.9)

    img_tmp = image[ha:hb, wa:wb]
    img_dst = cv2.resize(img_tmp, (w, h))

    return img_dst


def video_shake(video_path, step=5, is_write=False):
    cap = cv2.VideoCapture(video_path)
    c = 1
    if is_write:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fource = cv2.VideoWriter(*'MJPG')
        video_writer = cv2.VideoWriter("dst.mp4", fource, fps, (640, 480))

    while cap.isOpened():
        rval, frame = cap.read()
        if c % step == 0:
            frame = video_shake_image(frame)

        if is_write:
            video_writer.write(frame)

        c += 1
        cv2.imshow('video', frame)
        cv2.waitKey(30)

    cap.release()


if __name__=='__main__':
    video_path = r'G:\BaiduYunDownload\3.mp4'
    video_shake(video_path)