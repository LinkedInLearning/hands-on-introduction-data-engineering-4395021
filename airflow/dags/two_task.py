from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner': 'sheen',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'catchup': False,
    'start_date': datetime(2024, 8, 17)
}

with DAG(
    dag_id='two_task_dag',
    description='a two task airflow dag',
    schedule_interval=None,
    default_args=default_args
) as dag:

    t0 = BashOperator(
        task_id='bash_task_0',
        bash_command='echo "First Airflow task !"'
    )
    t1 = BashOperator(
        task_id='bash_task_1',
        bash_command='echo "Sleeping..." && sleep 5s && echo "Second airflow task"'
    )

    t0 >> t1
