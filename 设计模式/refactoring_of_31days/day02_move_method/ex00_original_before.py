#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex00_original_before.py"""


class Subject:

    def handle(self):
        pass


class Target:

    def __init__(self):
        self.__subject = Subject()

    def request(self):
        self.__subject.handle()
