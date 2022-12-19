#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/12/15 3:13 PM 
# ide： PyCharm

import sys
from typing import Tuple

from pyspark.rdd import RDD
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sort <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonSort") \
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r.value)
    sortedCount = lines.map(lambda x: (int(x), 1)).sortByKey()
    # This is just a demo on how to bring all the sorted data back to a single node.
    # In reality, we wouldn't want to collect all the data to the driver node.
    output = sortedCount.collect()
    for (num, unitcount) in output:
        print(num)

    spark.stop()
