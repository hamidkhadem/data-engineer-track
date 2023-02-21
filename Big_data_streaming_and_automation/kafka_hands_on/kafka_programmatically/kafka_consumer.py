from kafka import KafkaConsumer

TOPIC_NAME = "first-topic"
KAFKA_BOOTSTRAP_SERVER = "localhost:9092"


def kafka_consume_msgs():
    print("kafka consumer initializing")

    consumer = KafkaConsumer(TOPIC_NAME,
                            bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
                            auto_offset_reset="earliest",
                            enable_auto_commit=True)
    
    print("Kafka consumer is connected successfully")
    for msg in consumer:
        print(f"Consumer message topic: {msg.topic} "
                f"value: {msg.value} ",
                f"header: {msg.headers} ",
                f"offset: {msg.offset}")
        
        msg_value = msg.value.decode("utf-8")
        print(f"Decoded msg is: {msg_value}")


if __name__ == "__main__":
    kafka_consume_msgs()