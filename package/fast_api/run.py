#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/24 11:38 AM 
# ide： PyCharm

if __name__ == '__main__':
    import uvicorn

    # print(cpu_count())
    uvicorn.run(app="main2:app",
                # host="0.0.0.0",
                port=5003,
                workers=1,  # cpu_count()
                # debug=False  # True
                )
