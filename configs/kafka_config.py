# weather_streaming_platform/configs/kafka_config.py

BOOTSTRAP_SERVER = "localhost:9092"

RAW_TOPIC = "raw-weather"

PROCESSED_TOPIC = "processed-weather"

DLQ_TOPIC = "dead-letter-weather"