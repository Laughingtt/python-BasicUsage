#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/24 10:28 AM 
# ide： PyCharm


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World 5004'


if __name__ == '__main__':
    app.run(port=5004)
