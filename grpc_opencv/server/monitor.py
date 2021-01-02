import os
import log
import time
import pynvml
import socket
import logging
import argparse
import subprocess
from collections import OrderedDict
import pdb

def get_runners(ip, server, gpu_list, port_list, workers, gpu=False):
    runners = OrderedDict()
    for idx, port in enumerate(port_list):
        if gpu:
            runner = "CUDA_VISIBLE_DEVICES={:} python3 -u {:} -i {:} -p {:} -w {:}".format(gpu_list[idx],
                                                                                           server,
                                                                                           ip,
                                                                                           port,
                                                                                           workers)
        else:
            runner = "python3 -u {:} -i {:} -p {:} -w {:}".format(server,
                                                                  ip,
                                                                  port,
                                                                  workers)

        runners[port] = runner

    return runners

def process(ip, gpu_list, port_list, workers, gpu=False, interval=60):
    cwd = os.getcwd()
    server = os.path.join(cwd, "server.py")
    host_name = socket.getfqdn(socket.gethostname())
    ip = socket.gethostbyname(host_name)

    runners = get_runners(ip, server, gpu_list, port_list, workers, gpu=gpu)

    while True:
        for port in port_list:
            try:
                print("connect to {:}:{:}".format(ip, port))
                sk = socket.socket()
                sk.connect((ip, port))
                sk.close()
            except:
                sk.close()
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) +
                      "server: {:}:{:} stopped!".format(ip, port))

                command = runners[port]
                subprocess.Popen(command, shell=True)

            time.sleep(interval)


def process_debug():
    port =7771
    try:
        sk = socket.socket()
        sk.connect((ip, port))
    except:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) +
              "server: {:}:{:} stopped!".format(ip, port))
    sk.close()

def get_port_list(ports):
    ports = ports.strip(";").split(";")
    ports = [int(p) for p in ports]

    return ports

def get_gpu_list(port_list, gpu=False):
    gpu_list = []
    if gpu:
        pynvml.nvmlInit()
        device_nums = int(pynvml.nvmlDeviceGetCount())
        if len(port_list) % device_nums != 0:
            assert "port length is {:}, the number of ports must be an integer multiple of 4".format(len(port_list))
        else:
            count = len(port_list) / device_nums
            for i, _ in enumerate(port_list):
                gpu_list.append(i//count)

        return gpu_list

def _parse_param():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', type=list, default=[7401, 7408], help='port')
    parser.add_argument('--port2', '-ps', type=str, default="7401;7408", help='port')
    parser.add_argument('--workers', '-w', type=int, default=4, help='worker number')
    parser.add_argument('-g', '--gpu', action='store_true')
    parser.add_argument('-d', '--verbose', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    FLAGS, unparsed = parser.parse_known_args()
    return FLAGS, unparsed

if __name__=="__main__":
    host_name = socket.getfqdn(socket.gethostname())
    ip = socket.gethostbyname()
    FLAGS, unparsed = _parse_param()
    FLAGS.ip = ip
    time.sleep(60)
    port_list = get_port_list(FLAGS.port2)
    gpu_list = get_gpu_list(port_list, gpu=FLAGS.gpu)
    process(FLAGS.ip, gpu_list, port_list, FLAGS.workers, gpu=FLAGS.gpu)





                                                                                                                  port))



