#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/2 12:08
# @Author : MarxZhao
# @File : opencv_rcg.py
# @Software: PyCharm

import os
import sys
import log
import json
import time
import yaml
import cv2
import requests
import numpy as np
import traceback
from utils import ConfigDict, string_to_cvmat, cvmat_to_string, png_processing
from collections import defaultdict

class OpenCV_RCG(object):

    def __init__(self, config):
        self.thresh = config.thresh
        self.max_types = config.max_types

    def get_image_data(self, image_url):
        response = requests.get(image_url)
        return response.content, response.status_code

    def get_image_buffer(self, trace_id, image_buffer, image_url):
        error_code = 0
        imagebuf = ""
        if image_url:
            imagebuf, status_code = self.get_image_data(image_url)
            if status_code != 200:
                error_code = -10002
                log.logging_error(trace_id, error_code, "image_url:{:}, pull image failed".format(image_url))
        elif image_buffer:
            imagebuf = image_buffer
        else:
            error_code = -10003
            log.logging_error(trace_id, error_code, "image_url:{:}, image is null.".format(image_url))

        if imagebuf:
            if "webp" in image_url or "WEBP" in str(imagebuf):
                img = string_to_cvmat(imagebuf, "webp")
                imagebuf = cvmat_to_string(img)

        return imagebuf, error_code

    def inference(self, trace_id, image_buffer, image_url, request_type=0):
        std = 0.
        score = 0.
        error_code = 0

        if request_type not in [0, 1]:
            error_code = -10004
            log.logging_error(trace_id, error_code, "image_url: {:}, request_type {:} if valid.".format(image_url,
                                                                                                        traceback.format_exc()))

            return score, std, error_code
        image_buffer, error_code = self.get_image_buffer(trace_id, image_buffer, image_url)

        if error_code:
            return score, std, error_code

        try:
            score = np.mean(string_to_cvmat(image_buffer))
            std = np.std(string_to_cvmat(image_buffer))
            error_code = 0
        except Exception as e:
            error_code = -10006
            log.logging_error(trace_id, error_code, "image_url: {:} opencv reg failed: {:}".format(image_url, traceback.format_exc()))


        return score, std, error_code
