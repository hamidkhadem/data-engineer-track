# Run Airflow with Python Virtual Environments
Ref: https://www.youtube.com/watch?v=z7xyNOF8tak


1. Create virtual environment
```
$ python3 -m venv airflow_venv
```

2. start the venv
```
$ source airflow_venv/bin/activate
```

3. From the official github repo:
https://github.com/apache/airflow

Install airflow using the below command
make sure to change the constraints-3.xx to your python version
```
$ pip install 'apache-airflow==2.5.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.10.txt"
 ```

4. After installation, export AIRFLOW_HOME to the desired directory
```
$ export AIRFLOW_HOME=.
```

5. Initialize the database with:
```
$ airflow db init
```

6. Check db connection
```
$ airflow db check
```

7. Start Airflow webserver:
```
$ airflow webserver -p 8080
```

8. Create a user for logging in
```
$ airflow users create \
    --username admin \
    --firstname fname \
    --lastname lname \
    --email admin@domain.com \
    --role Admin
```

9. Open another terminal and start airflow scheduler
```
$ export AIRFLOW_HOME=.
$ airflow scheduler
```

****

### To rerun Airflow again
* Terminal_1:
```
$ export AIRFLOW_HOME=.
$ airflow webserver -p 8080
```
* Terminal_2:
```
$ export AIRFLOW_HOME=.
$ airflow scheduler
```
