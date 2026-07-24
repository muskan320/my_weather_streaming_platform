from kafka import KafkaConsumer
import json
from configs.kafka_config import (
    BOOTSTRAP_SERVER,
    RAW_TOPIC
)
from database.weather_repository import insert_weather_event

#create kafka consumer 
consumer=KafkaConsumer(
   RAW_TOPIC,
   bootstrap_servers= BOOTSTRAP_SERVER,
   group_id="weather-consumer-group",
   auto_offset_reset="earliest",
   enable_auto_commit=True,
   value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print(f"listening to raw topic: {RAW_TOPIC}")

try:
    for message in consumer:
        print(f"topic : {message.topic}")
        print(f"ofset : {message.offset}")
        print(f"key: {message.key}")
        print(f"value: {message.value}")
        insert_weather_event(message.value)
except KeyboardInterrupt:
    print("consumer stpped by user")
finally:
    consumer.close()
    print("kafka consumer closed successfully")