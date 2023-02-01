from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator


# normal function
def print_hello():
    return "This is the running of the python function"

python_dag = DAG(dag_id="simple_python_dag",
                description="a second method of running a dag",
                schedule_interval="0 0 * * *",
                start_date=datetime(2023, 2, 1),
                catchup=False)

bash_task = BashOperator(task_id="bash_task",
                        bash_command="echo This is from the second run")

python_task = PythonOperator(
    task_id="python_task",
    python_callable=print_hello,
    dag=python_dag
)

bash_task >> python_task