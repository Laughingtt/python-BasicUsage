#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/29 9:57 AM 
# ide： PyCharm


from server import GrpcChannelServer

if __name__ == "__main__":
    server = GrpcChannelServer(party_id="9999")
    # server.stop()
