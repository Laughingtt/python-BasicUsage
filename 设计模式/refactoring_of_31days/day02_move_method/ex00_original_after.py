#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ex00_original_before.py"""

class Subject: pass

class Target:
    def handle(self): pass
    def request(self): self.handle()
