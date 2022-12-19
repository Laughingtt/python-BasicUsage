#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/29 10:16 AM 
# ide： PyCharm

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, escape, request

flask_app = Flask(__name__)


@flask_app.route("/v2")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"


@flask_app.route("/v1")
def flask_main2():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask v1!"


app = FastAPI()


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}


app.mount("/", WSGIMiddleware(flask_app))
