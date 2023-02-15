#!/bin/sh
sqlite3 manual-etl-database.db <<EOF
.read create_tables.sql
.quit
EOF

sqlite3 airflow-etl-database.db <<EOF
.read create_tables.sql
.quit
EOF
