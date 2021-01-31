#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 14:48
# @Author : MarxZhao
# @File : video_process_base.py
# @Software: PyCharm

import cv2
import glob
import os
#opencv对视频读取有2GB大小限制


def test():
    cv2.namedWindow('Video')
    cap = cv2.VideoCapture(0)
    video_writer = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                   cap.get(cv2.CAP_PROP_FPS),
                                   (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    success, frame = cap.read()

    while success and not cv2.waitKey(10) == 27:
        blur = cv2.GaussianBlur(frame, (3, 3), 0)
        video_writer.write(blur)



def show():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return

    while True:
        _, frame = cap.read()
        cv2.imshow('result', frame)
        cv2.waitKey(30)

#图片合并成视频
def imgs2video(imgs_dir, save_name, fps=30):
    fource = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter(save_name, fource, fps, (640, 480))
    # imgs = glob.glob(os.path.join(imgs_dir, '*.jpg'))
    imgs = os.listdir(imgs_dir)
    for i in range(len(imgs)):
        img_name = os.path.join(imgs_dir, imgs[i])
        frame = cv2.imread(img_name)
        video_writer.write(frame)
        video_writer.release()

#视频合并
def videos2video(videos_dir):
    video_merge = cv2.VideoWriter("merge.avi", cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 24, (600, 480))
    videos = os.listdir(videos_dir)
    for v in videos:
        cap = cv2.VideoCapture(v)
        fps = cap.get(cv2.CAP_PROP_FPS)
        if cap.isOpened():
            i = 0
            while i < fps * 17.5:
                i += 1
                ret, prev = cap.read()
                if ret is True:
                    if fps == 24:
                        video_merge.write(prev)
                    else:
                        video_merge.write(prev)
                else:
                    break

    video_merge.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    show()


