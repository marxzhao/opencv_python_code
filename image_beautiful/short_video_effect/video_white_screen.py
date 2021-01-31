#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 16:32
# @Author : MarxZhao
# @File : video_white_screen.py
# @Software: PyCharm

import cv2
import numpy as np

#白闪也可以考虑mask addWeighted直加操作

def video_white_screen(image, gamma):
    gamma_table = [np.power(x/255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    return cv2.LUT(image, gamma_table)


def video_white_screen_show(video_path, step=5, is_write=False):
    cap = cv2.VideoCapture(video_path)
    c = 1
    if is_write:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fource = cv2.VideoWriter(*'MJPG')
        video_writer = cv2.VideoWriter("dst.mp4", fource, fps, (640, 480))

    while cap.isOpened():
        rval, frame = cap.read()
        print(c)
        if c % step == 0:
            frame = video_white_screen(frame, 0.3)

        if is_write:
            video_writer.write(frame)

        c += 1
        cv2.imshow('video', frame)
        cv2.waitKey(30)

    cap.release()


if __name__=="__main__":
    video_path = r'G:\BaiduYunDownload\AV\3.mp4'
    video_white_screen_show(video_path)