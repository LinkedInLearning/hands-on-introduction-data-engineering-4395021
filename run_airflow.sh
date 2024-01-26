export AIRFLOW_HOME="/workspaces/hands-on-introduction-data-engineering-4395021/airflow"
echo "AIRFLOW_HOME is set to: $AIRFLOW_HOME"

airflow webserver -D
airflow scheduler -D