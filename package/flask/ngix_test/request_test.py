#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/1 10:17 AM 
# ide： PyCharm

import requests

url = "http://127.0.0.1:8088/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "x_app": "5004",
}
headers = headers

r = requests.get(url=url, headers=headers)
print(r.text)
