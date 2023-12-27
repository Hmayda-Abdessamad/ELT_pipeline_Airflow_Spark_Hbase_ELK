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
    'start_date': datetime(2023, 10, 1),
    'email': ['abdoessamadhmayda@gmail.com'],
    'timezone': system_timezone,
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(  dag_id = "historical_data",default_args=args, schedule_interval = "@monthly")

start = PythonOperator(
    task_id="start",
    python_callable = lambda: print("Jobs started"),
    dag=dag
)

historical_data = SparkSubmitOperator(
    task_id="Get_historical_data",
    conn_id="spark-conn",
    application="jobs/python/historical_data.py",
    dag=dag
)

historical_data_preprocess = SparkSubmitOperator(
    task_id="historical_data_preprocess",
    conn_id="spark-conn",
    application="jobs/python/Historical_data_preprocess.py",
    dag=dag
)

end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)



start>>historical_data>>historical_data_preprocess>>end