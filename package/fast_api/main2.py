#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/24 11:16 AM 
# ide： PyCharm

from fastapi import FastAPI

app = FastAPI()

dic = {}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/put")
async def root1(name: str):
    print(name)
    dic[name] = 2
    return dic
