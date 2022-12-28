#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/28 11:43 AM 
# ide： PyCharm

import sys
import logging

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
print("====")
logging.debug("1234")
logging.info("1234")
logging.info(f"{122} train time: {333}")
print("====")
