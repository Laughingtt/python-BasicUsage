# from operator import add

# from arch.api import session
# from arch.api.impl.based_spark._materialize import materialize
# from arch.api.impl.based_spark._table import RDDTable
# from arch.common import hdfs_utils

if __name__ == '__main__':
    # table=RDDTable()
    # session.init(mode=0, backend=1, job_id="a_great_session")
    # t = [(10, 20), (30, 40), (50, 60), (50, 60)]
    # table: RDDTable = session.parallelize(data=t,include_key=True, partition=1)
    # print(table.collect())
    # print(table)

    hdfs1 = 'hdfs://10.10.10.241:19000/data/id_2000.csv'
    hdfs2 = 'hdfs://10.10.10.241:19000/data/guest_data.csv'

    from pyspark import SparkContext

    sc = SparkContext.getOrCreate()
    data = sc.textFile(hdfs1, 1).repartition(8).map(lambda v: "upai_" + v)
    data.saveAsPickleFile("hdfs://10.10.10.241:19000/data/upai_id")
    print(data.take(3))
