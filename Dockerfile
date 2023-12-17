FROM apache/airflow:2.7.1-python3.11

USER root
RUN rm /etc/apt/sources.list.d/mysql.list


RUN apt-get update && \
    apt-get install -y gcc  && \
    apt-get install -y python3-dev && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;


# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

COPY requirement_airflow.txt /requirement_airflow.txt

RUN pip install --upgrade pip \
    && pip install --no-cache-dir  -r /requirement_airflow.txt
