from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVER = "localhost:9092"


def kafka_producer_msg(topic_name, msg, msg_header):
    print("Kafka producer is initializing")
    producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
                             acks=1,
                             retries=3,
                             reconnect_backoff_max_ms=10000)
    
    if producer.bootstrap_connected():
        print("Kafka producer connected successfully")
        msg_to_send = str(msg).encode()
        msg_sent = producer.send(topic_name,
                                msg_to_send,
                                headers=[("message_type", msg_header.encode())]
                                )
        
        msg_sent.add_callback(on_send_success)

        producer.flush()

def on_send_success(record):
    print(f"Message send to topic: {record.topic}")
    print(f"on partition: {record.partition}")
    print(f"on offset: {record.offset}")


if __name__ == "__main__":
    kafka_producer_msg("first-topic", "another message", "Testing_header")
