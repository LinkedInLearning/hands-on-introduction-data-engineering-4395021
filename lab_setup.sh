#!/bin/sh

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


