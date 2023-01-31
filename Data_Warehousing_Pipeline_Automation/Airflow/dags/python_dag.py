from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

# Normal python function
def print_hello():
    return 'Hello world from first Airflow DAG!'

# Defining an airflow dag
python_dag = DAG('simple_python_dag',
          description='Simple Python DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2022, 1, 1), catchup=False)

# Defining a bash opertor
bash_task = BashOperator(
    task_id="bash_task",
    bash_command="echo hello")

# Defining a python operator
python_task_1 = PythonOperator(
    task_id='python_task',
    python_callable=print_hello,
    dag=python_dag)

bash_task >> python_task_1
