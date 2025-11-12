FROM apache/spark:3.5.1

USER root
WORKDIR /opt/spark

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

# Create jars dir and download Hadoop AWS + AWS SDK jars for S3A
RUN mkdir -p /opt/spark/jars && \
    wget -q https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar -P /opt/spark/jars && \
    wget -q https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.767/aws-java-sdk-bundle-1.12.767.jar -P /opt/spark/jars

# Copy your PySpark jobs
COPY ./spark_jobs /opt/spark/jobs

# Optional: copy spark-defaults.conf if you add it to repo
# COPY ./spark/conf/spark-defaults.conf /opt/spark/conf/spark-defaults.conf

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

CMD ["/bin/bash"]
