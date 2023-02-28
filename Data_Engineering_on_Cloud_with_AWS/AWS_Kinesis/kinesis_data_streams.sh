aws --version

aws kinesis put-record --stream-name demoStream --partition-key app1 --data "create user" --cli-binary-format raw-in-base64-out


aws kinesis describe-stream --stream-name demoStream

aws kinesis get-shard-iterator --stream-name demoStream --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON

aws kinesis get-records --shard-iterator
