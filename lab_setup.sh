#!/bin/sh

# Turn off SQLALCHEMY Warning
export SQLALCHEMY_SILENCE_UBER_WARNING=1
echo 'export SQLALCHEMY_SILENCE_UBER_WARNING=1' >> ~/.bashrc 

# Set Airflow home
export AIRFLOW_HOME="/workspaces/hands-on-introduction-data-engineering-4395021/airflow"
echo 'export AIRFLOW_HOME="/workspaces/hands-on-introduction-data-engineering-4395021/airflow"' >> ~/.bashrc 

# Some Setup + Install some helpful libs
pip install --upgrade pip
pip install connexion[swagger-ui]
pip install graphviz

# Paths
export LAB_BASE_PATH=`pwd`/lab
export LAB_MANUAL_PATH="$LAB_BASE_PATH/manual"
export LAB_ORCHESTRATED_PATH="$LAB_BASE_PATH/orchestrated"
export LAB_END_TO_END_PATH="$LAB_BASE_PATH/end-to-end"
export LAB_TEMP_PATH="$LAB_BASE_PATH/temp"
export LAB_CHALLENGE_PATH="$LAB_BASE_PATH/challenge"
export LAB_AIRFLOW_PATH="$LAB_BASE_PATH/airflow"


# Manual Sqlite Database
sqlite3 "$LAB_MANUAL_PATH/manual-load-db.db" <<EOF
.read create_table.sql
.quit
EOF

# Airflow Sqlite Database
sqlite3 "$LAB_ORCHESTRATED_PATH/airflow-load-db.db" <<EOF
.read create_table.sql
.quit
EOF

# Basic Etl Sqlite Database
sqlite3 "$LAB_END_TO_END_PATH/basic-etl-load-db.db" <<EOF
.read create_table.sql
.quit
EOF

# Challenge Sqlite Database
sqlite3 "$LAB_CHALLENGE_PATH/challenge-load-db.db" <<EOF
.read create_challenge_table.sql
.quit
EOF
 
# Source bashrc
source ~/.bashrc 