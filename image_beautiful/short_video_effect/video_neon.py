#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 16:42
# @Author : MarxZhao
# @File : video_neon.py
# @Software: PyCharm

import cv2
import numpy

#正确思路，使用neon 的mask addweighted

def video_neon_image(image):
    h, w, c = image.shape
    ha = int(h * 0.9)
    wb = int(w * 0.1)
    cv2.circle(image, (wb, ha), 20, (114, 128, 250), -1)
    cv2.circle(image, (wb+40, ha-40), 20, (106, 106, 250), -1)
    cv2.circle(image, (wb+80, ha), 20, (114, 128, 250), -1)
    cv2.circle(image, (wb, ha-60), 20, (124, 128, 250), -1)

    return image


def video_neon(video_path, step=5, is_write=False):
    cap = cv2.VideoCapture(video_path)
    c = 1
    if is_write:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fource = cv2.VideoWriter(*'MJPG')
        video_writer = cv2.VideoWriter("dst.mp4", fource, fps, (640, 480))

    while cap.isOpened():
        rval, frame = cap.read()
        if c % step == 0:
            frame = video_neon_image(frame)

        if is_write:
            video_writer.write(frame)

        c += 1
        cv2.imshow('video', frame)
        cv2.waitKey(30)

    cap.release()


if __name__=='__main__':
    video_path = r'G:\BaiduYunDownload\AV\3.mp4'
    video_neon(video_path)