# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:hello_server.py
@time:2021/10/09

"""
# !/usr/bin/env python
# -*-coding: utf-8 -*-

from concurrent import futures
import grpc
import logging
import time

from rpc_package.transfer_pb2_grpc import add_TransferServerServicer_to_server, \
    TransferServerServicer
from rpc_package.transfer_pb2 import Message, RequestMeta, Empty


class Hello(TransferServerServicer):

    # 这里实现我们定义的接口
    def recv(self, request, context):
        print("hello {}".format(request))
        return Empty()


def serve():
    # 这里通过thread pool来并发处理server的任务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 将对应的任务处理函数添加到rpc server中
    add_TransferServerServicer_to_server(Hello(), server)

    # 这里使用的非安全接口，世界gRPC支持TLS/SSL安全连接，以及各种鉴权机制
    server.add_insecure_port('[::]:50000')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    serve()
