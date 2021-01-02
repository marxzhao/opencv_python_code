#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/2 20:57
# @Author : MarxZhao
# @File : client.py
# @Software: PyCharm

import uuid
import time
import grpc
import logging
import argparse
import traceback
import concurrent.futures
import os
import random
from proto.opencv_proto import opencv_pb2
from proto.opencv_proto import opencv_pb2_grpc
import pdb

def get_trace_id(trace_id=None):
    if trace_id:
        return trace_id

    return str(uuid.uuid1())

def run(ip="127.0.0.1", port=5000):
    with open("data/1.jpg", "rb") as fr:
        inputbuf = fr.read()

    try:
        trace_id = get_trace_id()
        options = [("grpc.max_send_message_length", 1024 * 1024 * 1024),
                   ("grpc.max_receive_message_leghth", 1024 * 1024 *1024)]

        with grpc.insecure_channel("{:}:{:}".format(ip, port), options=options) as channel:
            stub = opencv_pb2_grpc.OpenCVStub(channel)
            request = opencv_pb2.OpenCVRequest()

            request.interface_mode = 1
            request.image_buffer = inputbuf
            request.request_type = 0
            request.trace_id = trace_id

            start = time.time()
            print(request)

            response = stub.RunOpenCV(request)
            print(response)
            print(response.results[0].fscore, response.results[0].fstd)
            cost = time.time() - start

    except Exception as err:
        logging.error(traceback.format_exc() + '\n')


if __name__=="__main__":
    ip = "127.0.0.1"
    run(ip, 5000)
