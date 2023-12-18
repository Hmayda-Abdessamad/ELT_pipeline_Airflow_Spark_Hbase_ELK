from datetime import datetime, timedelta

from airflow import DAG
import pendulum
from airflow.models import Connection
from airflow.utils import db
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

system_timezone = pendulum.local_timezone()

#create a conn

db.merge_conn( Connection( conn_id="spark-conn", conn_type="spark", host="spark://spark-master",port=7077 ))

#default argument for our dag , this dag will be trigged every month

args = {

    'owner': 'HMAYDA',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email': ['abdoessamadhmayda@gmail.com'],
    'timezone': system_timezone,
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(  dag_id = "ELT_pipeliine",default_args=args, schedule_interval = "@monthly")

start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)


python_job = SparkSubmitOperator(
    task_id="Historical_data",
    conn_id="spark-conn",
    application="jobs/python/historical_data.py",
    dag=dag
)

end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

start >> python_job >> end
