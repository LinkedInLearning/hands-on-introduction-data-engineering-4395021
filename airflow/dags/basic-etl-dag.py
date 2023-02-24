from airflow import DAG
from datetime import datetime, date
from airflow.operators.python import PythonOperator
import pandas as pd

with DAG(
    dag_id='basic_etl_dag',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id='extract_task',
        bash_command='wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/end-to-end/basic-etl-extract-data.csv',
    )

  def transform_data():
      """Read in the file, and write a transformed file out"""
      today = date.today()
      df = pd.read_csv("/workspaces/hands-on-introduction-data-engineering-4395021/lab/end-to-end/basic-etl-extract-data.csv")
      generic_type_df = df[df["Type"] == "generic"]
      generic_type_df["Date"] = today.strftime("%Y-%m-%d")
      generic_type_df.to_csv("/workspaces/hands-on-introduction-data-engineering-4395021/lab/end-to-end/basic-etl-transform-data.csv", index=False)
      print(f'Number of rows: {len(generic_type_df)}')

  transform_task = PythonOperator(
       task_id='transform_task',
       python_callable=transform_data,
       dag=dag)

  Transform_task

 load_task = BashOperator(
        task_id='load_task', 
        bash_command='echo -e ".separator ","\n.import /workspaces/hands-on-introduction-data-engineering-4395021/lab/end-to-end/basic-etl-transform-data.csv top_level_domains" | sqlite3 /workspaces/hands-on-introduction-data-engineering-4395021/lab/end-to-end/basoc-etl-load-db.db',
        dag=dag
    )


    extract_task >> transform_task >> load_task

