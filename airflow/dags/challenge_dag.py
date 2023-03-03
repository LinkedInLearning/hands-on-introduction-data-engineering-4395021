''' Challenge'''
from datetime import datetime, date
import pandas as pd
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG

with DAG(
    dag_id='challenge_dag',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False) as dag:

    extract_task = BashOperator(
        task_id='extract_task',
        bash_command='wget -c https://datahub.io/core/s-and-p-500-companies/r/constituents.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-extract-data.csv'
        )

    def transform_data():
        """Read in the file, and write a transformed file out"""
        today = date.today()
        df = pd.read_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-extract-data.csv')
        count_df = df.groupby(["Sector"])["Sector"].count().reset_index(name="count")
        count_df['Date'] = today.strftime('%Y-%m-%d')
        count_df.to_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-transform-data.csv', index=False)

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
        dag=dag)

    load_task = BashOperator(
        task_id='load_task',
        bash_command='echo -e ".separator ","\n.import --skip 1 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-transform-data.csv sp_500_sector_count" | sqlite3 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-load-db.db',
        dag=dag)

    extract_task >> transform_task >> load_task

