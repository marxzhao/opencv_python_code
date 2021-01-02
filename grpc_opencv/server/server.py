#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/2 19:31
# @Author : MarxZhao
# @File : server.py
# @Software: PyCharm


import os
import sys
import log
import json
import time
import yaml
import uuid
import grpc
import base64
import logging
import operator
import argparse
import traceback
import configparser
from proto.opencv_proto import opencv_pb2
from proto.opencv_proto import opencv_pb2_grpc
from utils import ConfigDict
from concurrent import futures
from opencv_rcg import OpenCV_RCG
import requests
import pdb

ONE_DAY_IN_SECONDS = 60 * 60 * 24

def init(config):
    yaml_data = yaml.load(open(config), Loader=yaml.FullLoader)
    config = ConfigDict(yaml_data)
    return config

def get_trace_id(trace_id=None):
    if trace_id:
        return trace_id

    return str(uuid.uuid1())

class Servicer(opencv_pb2_grpc.OpenCVServicer):
    def __init__(self, config, ip, port):
        logging.info("OpenCV Servicer init.")
        self.op = None
        self.op = OpenCV_RCG(config)
        self.ip = ip
        self.port = port

    def run(self, imagebuf, image_url, context_id, trace_id):
        std = 0.
        score = 0.
        error_code = 0
        try:
            std, score, error_code = self.op.inference(trace_id, imagebuf, image_url)
            print(std, score, error_code)
        except Exception as e:
            error_code = -10011
            log.logging_error(trace_id, error_code, "OpenCV server failed: {:}".format(traceback.format_exc()))

        response = opencv_pb2.OpenCVResponse(trace_id=trace_id, context_id=context_id, error_code=error_code)
        print(response)
        for i in range(1):
            item = response.results.add()
            item.fscore = score
            item.fstd = std

        return response

    def RunOpenCV(self, request, context):
        metadata = dict(context.invocation_metadata())
        _, peer_ip, peer_port = context.peer().split(':')
        ip = metadata.get('x-real-ip', peer_ip)
        port = metadata.get('x-real-port', peer_port)
        client = "{:}:{:}".format(ip, port)

        image_buffer = request.image_buffer
        image_url = request.image_url
        context_id = request.context_id
        trace_id = request.trace_id

        start = time.time()
        res = self.run(image_buffer, image_url, context_id, trace_id=trace_id)
        cost = time.time() - start

        logging.info('request info: trace_id: {:}, client: {:} error_code: {:}, cose: {:}, image_url: {:}'.format(trace_id,
                                                                                                                  client,
                                                                                                                  res.error_code,
                                                                                                                  cost,
                                                                                                                  image_url))
        return res


def serve(config, ip="127.0.0.1", port=5000, process_workers=1):
    try:
        logging.info('server init')
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=process_workers), options=[
            ('grpc.max_send_message_length', 500 * 1024 * 1024),
            ('grpc.max_receive_message_length', 500 * 1024 * 1024)])
        print('aa', config, ip, port)
        opencv_pb2_grpc.add_OpenCVServicer_to_server(Servicer(config, ip, port), server)
        print('dst')
        server.add_insecure_port("{:}:{:}".format(ip, port))
        print('dst1')
        server.start()
        logging.info('server ready')
    except KeyboardInterrupt:
        server.stop(0)

    except Exception as e:
        server.stop(0)
        logging.error('Exception:{}'.format(traceback.format_exc()))

    while True:
        time.sleep(ONE_DAY_IN_SECONDS)


def _parse_param():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', type=str, default="data/config.yaml", help='config')
    parser.add_argument('--port', '-p', type=int, default=5000, help='port')
    parser.add_argument('--ip', '-i', type=str, default='127.0.0.1', help='ip address')
    parser.add_argument('--workers', '-w', type=int, default=1, help='worker number')
    parser.add_argument('-d', '--verbose', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    FLAGS, unparsed = parser.parse_known_args()
    return FLAGS, unparsed

if __name__=="__main__":
    FLAGS, unparsed = _parse_param()
    log.init_logging('log/{}/server_{}.log'.format(FLAGS.ip, FLAGS.port),
                     verbose=FLAGS.verbose, level="INFO")

    config = init(FLAGS.config)
    print(config)

    serve(config, FLAGS.ip, FLAGS.port, FLAGS.workers)