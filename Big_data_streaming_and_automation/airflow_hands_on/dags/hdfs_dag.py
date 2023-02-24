from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


dag_hdfs = DAG(
    dag_id="hdfs_example_dag",
    default_args={"retries": 2},
    schedule_interval="0 0 * * *",
    start_date=days_ago(1),
    description="executing hdfs commands"
)

print("Creating a directory")
create_dir = BashOperator(
    task_id="create_dir",
    bash_command="hdfs dfs -mkdir /user/airflow",
    dag=dag_hdfs
)

print("Giving permissions to directory")
give_permissions = BashOperator(
    task_id="give_permissions",
    bash_command="hdfs dfs -chmod -R 777 /user/airflow",
    dag=dag_hdfs
)

print("listing hdfs user directories")
list_all_users = BashOperator(
    task_id="list_files",
    bash_command="hdfs dfs -ls /user/",
    dag=dag_hdfs
)

create_dir>>give_permissions>>list_all_users