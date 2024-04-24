''' Extract DAG '''
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

with DAG('extract_dag',
         schedule_interval=None,
         start_date=datetime(2022, 1, 1),
         catchup=False) as dag:
        
    # The location of the top-level-domain-names.csv file has changed. Now, it is hosted in the same repository as this project.
    extract_task = BashOperator(
            task_id='extract_task',
            bash_command='wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/main/data/top-level-domain-names.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv'
            )
