from kafka import KafkaConsumer
from functools import wraps
import time
from random import random


def backoff(tries, sleep):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed retry {i}: {e}")
                    time.sleep(sleep / 10)
            raise Exception("All retries failed.")
        return wrapper

    return inner


@backoff(tries=5, sleep=1)
def message_handler(value) -> None:
    if random() < 0.3:
        raise Exception("Fake retry")
    print(value)


def create_consumer():
    print("Connecting to Kafka brokers")
    consumer = KafkaConsumer("sinaya",
                             group_id='sinaya_fail_retries',
                             bootstrap_servers='localhost:29092',
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)

    for message in consumer:
        # send to http get (rest api) to get response
        # save to db message (kafka) + external
        message_handler(message)
        print(message)


if __name__ == '__main__':
    create_consumer()
