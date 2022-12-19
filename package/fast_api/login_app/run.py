#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/24 11:12 PM 
# ide： PyCharm

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app",
                workers=1)