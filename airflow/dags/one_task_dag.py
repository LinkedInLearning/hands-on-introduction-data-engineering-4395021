'''ONE TASK DAG'''

from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner':'sheen',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':0,
    'catchup':False,
    'start_date':datetime(2024,8,16)
}

with DAG(
    dag_id='one_task_dag',
    description='a one task airflow dag',
    schedule_interval=None,
    default_args=default_args
    )as dag:

    task1 = BashOperator(
        task_id = 'one_task',
        bash_command='echo "hello, linkedin learning" > /workspaces/hands-on-introduction-data-engineering-4395021/airflow/dags/created_file.txt',
        dag=dag
    )