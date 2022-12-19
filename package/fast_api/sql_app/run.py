#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/25 12:05 AM 
# ide： PyCharm

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app",
                workers=1)
