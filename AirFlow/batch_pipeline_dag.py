from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'de_student',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='batch_pipeline_quarterly',
    default_args=default_args,
    start_date=datetime(2024,1,1),
    schedule_interval='0 2 1 */3 *',
    catchup=False,
    max_active_runs=1,
) as dag:

    ingest = BashOperator(
        task_id='ingest_csv_to_minio',
        bash_command='docker exec ingestion python /app/ingestion/app.py'
    )

    spark_etl = BashOperator(
        task_id='spark_etl',
        bash_command='docker exec spark-master spark-submit --master spark://spark-master:7077 /opt/spark/jobs/etl_job.py'
    )

    ingest >> spark_etl
