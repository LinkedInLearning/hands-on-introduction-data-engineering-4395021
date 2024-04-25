
'''Challenge ETL'''

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
import pandas as pd
from datetime import datetime, date

with DAG(
    dag_id='challenge_dag',
    start_date=datetime(2024,4,25),
    catchup=False,
    schedule_interval=None,
         )as dag:
    
    extract_task = BashOperator(
        task_id = 'extract_task',
        bash_comand = "wget -c https://raw.githubusercontent.com/LinkedInLearning/hands-on-introduction-data-engineering-4395021/b82f29e0eaed61a398a1f6f81b547590e3ac78fd/data/constituents.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/data.csv"
    )

    def transform_data():
        '''Aggregate the data to get the count of each sector in S&P 500 data'''
        filepath = '/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/data.csv'
        df=pd.read_csv(filepath)
        df_agg_sp = df['Sector'].value_counts().reset_index()
        df_agg_sp.columns = ['Sector','Count']
        today = date.today()
        df_agg_sp['Date']=today.strftime('%Y-%m-%d')
        df_agg_sp.to_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/data-transform.csv', index=False)

    transform_task = PythonOperator(
        task_id = 'transform_task',
        python_callable=transform_data,
        dag=dag
    )

    load_task =BashOperator(
        task_id ='load_task',
        bash_command = 'echo -e ".separator ","\n.import --skip 1 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/data-transform.csv sp_500_sector_count" | sqlite3 /workspaces/hands-on-introduction-data-engineering-4395021/lab/challenge/challenge-load-db.db',
        dag=dag
    )

    extract_task >> transform_task >> load_task
