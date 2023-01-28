#!/bin/sh

var1=$1
var2=$(date)
echo "Before running python code"
echo "Date is: $var2"

echo "Running the python code"
python3 ./run_with_shell.py $var1 "$var2"

echo "Done with running python code"