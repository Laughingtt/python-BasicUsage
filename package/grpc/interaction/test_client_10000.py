#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/29 4:48 PM 
# ide： PyCharm

from grpc_channel_client import GrpcChannelClient


class Host(GrpcChannelClient):

    def test_remote(self):
        client.remote("273872837823", 9999, "host_to_guest")

    def test_get(self):
        res = client.get(9999, "guest_to_host")
        print("get res is ", res)

        res = client.get(9999, "guest_to_host2")
        print("get res is ", res)


if __name__ == '__main__':
    client = Host(party_id="10000")
    client.test_remote()
    client.test_get()
