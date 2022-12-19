#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/24 11:29 AM 
# ide： PyCharm
import time
import requests

t0 = time.time()
for i in range(1000):
    r = requests.get(url='http://127.0.0.1:5001/')
    print(r)

print(time.time()-t0)