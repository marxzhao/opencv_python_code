#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/24 15:14
# @Author : MarxZhao
# @File : video_time_regorge.py
# @Software: PyCharm

import cv2
import numpy

def video_time_regorge(video_path, step=5, is_write=False):
    cap = cv2.VideoCapture(video_path)
    c = 1
    if is_write:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fource = cv2.VideoWriter(*'MJPG')
        video_writer = cv2.VideoWriter("dst.mp4", fource, fps, (640, 480))

    frames = []
    while cap.isOpened():
        rval, frame = cap.read()
        frames.append(frame)
        # cv2.waitKey(30)
    cap.release()

    for i in range(len(frames), 0, -1):
        cv2.imshow('video', frames[i])


if __name__=='__main__':
    video_path = r'G:\BaiduYunDownload\AV\3.mp4'
    video_time_regorge(video_path)