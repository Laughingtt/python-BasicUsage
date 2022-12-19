#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/29 2:40 PM 
# ide： PyCharm

from flask import Flask, escape, request

flask_app = Flask(__name__)


@flask_app.route("/v1")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"


if __name__ == '__main__':
    flask_app.run(port=8001)