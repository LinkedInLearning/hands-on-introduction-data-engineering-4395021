from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
		'owner' : 'Vinoo',
		'depends_on_past' :False,
		'email' :['email@example.com'],
		'email_on_failure': False,
		'email_on_retry': False,
		'catchup': False,
		'retries': 0,
		'retry_delay': timedelta(minutes=5)
		}

dag = DAG(
	'CreateFile',
	default_args=default_args,
	start_date=datetime(2023,1,1,0,0))


task1 = BashOperator(
		task_id='prove_things_work',
		bash_command='echo "hello, world!" > /home/codespace/temp/create-this-file.txt',
		dag=dag)
