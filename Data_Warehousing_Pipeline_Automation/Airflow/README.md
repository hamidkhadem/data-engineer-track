# Docker-compose setup commands

* Use the docker-compose file in this repo: docker-compose.yaml

* Make sure the following directories already created when cloning the repo:
./dags ./logs ./plugins ./.env

* If not, run the following commands:

```
$ mkdir -p ./dags ./logs ./plugins
$ echo -e "AIRFLOW_UID=$(id -u)" > .env
```

* Initialize the database by running database migrations and create the first user account. To do this, run.
```
docker-compose up airflow-init
```

* After initialization is complete, you should see a message like this:
```
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.4.1
start_airflow-init_1 exited with code 0
```

* Running Airflow: 
```
docker-compose up -d
```

* Access the web user-interface at: `http://localhost:8080` . 
The default account has the login `airflow` and the password `airflow` .
