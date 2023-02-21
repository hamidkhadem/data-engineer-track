Ref: https://towardsdatascience.com/pyflink-how-to-create-a-table-from-a-csv-source-ca4851a71d0c

### **Make sure to have python3.9 for this example to work**

* Create flink_venv virtual environment
```
$ python3.9 -m venv flink_venv
```

* Activate the environment
```
$ source flink_venv/bin/activate
```

* Download Apach Flink library
```
$ python3.9 -m pip install protobuf==3.17
$ python3.9 -m pip install apache-flink
```

* Run the example
```
$ python3.9 ./pyflink_table_csv.py
```
