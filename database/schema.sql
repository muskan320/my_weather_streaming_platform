CREATE DATABASE IF NOT EXISTS weather_db;

USE weather_db;

CREATE TABLE IF NOT EXISTS weather_readings (

    id BIGINT AUTO_INCREMENT PRIMARY KEY,

    city VARCHAR(100),

    temperature_c FLOAT,

    humidity_percent FLOAT,

    wind_speed_kmh FLOAT,

    pressure_hpa FLOAT,

    condition_name VARCHAR(100),

    event_time DATETIME,

    kafka_partition INT,

    kafka_offset BIGINT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);