#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/29 4:48 PM 
# ide： PyCharm


from grpc_channel_client import GrpcChannelClient
from rpc_package.transfer_pb2 import Message, RequestMeta, Party


class Guest(GrpcChannelClient):

    def test_remote(self):
        client.remote("123454567", 10000, "guest_to_host")

    def test_get(self):
        res = client.get(10000, "host_to_guest")
        print("get res is ", res)


if __name__ == '__main__':
    client = Guest(party_id="9999")
    client.test_remote()
    client.test_get()
