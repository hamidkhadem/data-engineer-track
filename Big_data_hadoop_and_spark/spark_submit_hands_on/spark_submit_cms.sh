spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --driver-memory 2g \
    --executor-memory 2g \
    --executor-cores 1 \
    pyspark_script.py