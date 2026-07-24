import os
import sys
import json

from kafka import KafkaProducer

from configs.kafka_config import (
    BOOTSTRAP_SERVER,
    RAW_TOPIC,
)
# CREATE KAFKA PRODUCER
producer=KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_serializer=lambda value:
      json.dumps(value).encode("utf-8")
)


def publish_event(event, key=None):

    print("1. Inside publish_event()")

    future = producer.send(
        topic=RAW_TOPIC,
        key=key.encode("utf-8") if key else None,
        value=event
    )

    print("2. producer.send() completed")

    return future

def publish_and_confirm(event,key=None):
    future=publish_event(event,key)
    metadata=future.get(timeout=10)
    return metadata

def close():
    producer.flush()
    producer.close()