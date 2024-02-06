from kafka import KafkaConsumer


def create_consumer():
    print("Connecting to Kafka brokers")
    consumer = KafkaConsumer("sinaya_processed3",
                             group_id='sinaya_processed_group3',
                             bootstrap_servers='localhost:29092',
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)

    for message in consumer:
        #save to DB
        print(message)


if __name__ == '__main__':
    create_consumer()
