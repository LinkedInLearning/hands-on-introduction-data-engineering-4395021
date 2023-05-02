#!/bin/bash
export AIRFLOW_HOME="/workspaces/hands-on-introduction-data-engineering-4395021/airflow"

AIRFLOW_VERSION=2.5.1
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
echo "Installing Airflow Version $AIRFLOW_VERSION, with Python $PYTHON_VERSION"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

airflow db init
sed -i -e '/WTF_CSRF_ENABLED =/ s/= .*/= False/' ${AIRFLOW_HOME}/webserver_config.py
sed -i -e '/load_examples =/ s/= .*/= False/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/dag_dir_list_interval =/ s/= .*/= 2/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/worker_refresh_batch_size =/ s/= .*/= 0/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/worker_refresh_interval =/ s/= .*/= 0/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/workers =/ s/= .*/= 2/' ${AIRFLOW_HOME}/airflow.cfg

airflow users create --username admin --firstname Firstname --lastname Lastname --role Admin --email admin@example.org --password password
airflow webserver -D
airflow scheduler -D
