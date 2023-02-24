#!/bin/sh

# Paths
export LAB_BASE_PATH=`pwd`/lab
export LAB_MANUAL_PATH="$LAB_BASE_PATH/manual"
export LAB_ORCHESTRATED_PATH="$LAB_BASE_PATH/orchestrated"
export LAB_ETL_PATH="$LAB_BASE_PATH/etl"
export LAB_TEMP_PATH="$LAB_BASE_PATH/temp"
export LAB_AIRFLOW_PATH="$LAB_BASE_PATH/airflow"


# Set some environment variables
export AIRFLOW__WEBSERVER__WORKER_REFRESH_BATCH_SIZE=0
export AIRFLOW__WEBSERVER__WORKER_REFRESH_INTERVAL=0
export AIRFLOW__WEBSERVER__WORKERS=2
export AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL=2

# Manual Sqlite Database
sqlite3 "$LAB_MANUAL_PATH/manual-etl-db.db" <<EOF
.read /workspaces/hands-on-introduction-data-engineering-4395021/create_table.sql
.headers on
.mode csv
.quit
EOF

# Airflow Sqlite Database
sqlite3 "$LAB_ORCHESTRATED_PATH/orchestrated-etl-db.db" <<EOF
.read /workspaces/hands-on-introduction-data-engineering-4395021/create_table.sql
.headers on
.mode csv
.quit
EOF

# Basic Etl Sqlite Database
sqlite3 "$LAB_ETL_PATH/basic-etl-database.db" <<EOF
.read /workspaces/hands-on-introduction-data-engineering-4395021/create_table.sql
.headers on
.mode csv
.quit
EOF
