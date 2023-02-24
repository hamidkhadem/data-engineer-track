from airflow import DAG
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.utils.dates import days_ago


dag_hive = DAG(
    dag_id="hive_example_dag",
    default_args={"retries": 2},
    schedule_interval="0 0 * * *",
    start_date=days_ago(1),
    description="executing hive commands"
)

DATABASE_NAME = "airflow_db"

print("creating a database")
create_db = HiveOperator(
    task_id="create_database",
    hql=(
        f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
    ),
    dag=dag_hive
)

print("show databases")
show_hive_dbs = HiveOperator(
    task_id="show_databases",
    hql=(
        f"SHOW DATABASES"
    ),
    dag=dag_hive
)

create_db>>show_hive_dbs