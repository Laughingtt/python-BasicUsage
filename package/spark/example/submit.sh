/data/spark/spark-2.4.3-bin-hadoop2.7/bin/spark-submit \
--master=spark://tiger.sh.udai.work:7077  \
--conf spark.pyspark.driver.python=/data/projects/water-drop-algo/python-env/venv/bin/python  \
--conf spark.pyspark.python=/data/projects/water-drop-algo/python-env/venv/bin/python  \
--executor-memory=2G  \
--driver-memory=1G  \
--total-executor-cores=2  \
--executor-cores=1 \
/data/spark/spark-2.4.3-bin-hadoop2.7/examples/src/main/python/pi.py 8