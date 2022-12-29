# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:hello_client.py
@time:2021/10/09

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import logging

import grpc
from rpc_package.transfer_pb2 import Message,RequestMeta
from rpc_package.transfer_pb2_grpc import TransferServerStub


def run():
    # 使用with语法保证channel自动close
    with grpc.insecure_channel('localhost:50051') as channel:
        # 客户端通过stub来实现rpc通信
        stub = TransferServerStub(channel)

        # 客户端必须使用定义好的类型，这里是HelloRequest类型
        m = Message()
        m.bytes.data = b'123'
        m.request_meta.CopyFrom(RequestMeta(tag="hello"))

        response = stub.recv(m)
    print("hello client received: {}".format(response))


if __name__ == "__main__":
    logging.basicConfig()
    run()


