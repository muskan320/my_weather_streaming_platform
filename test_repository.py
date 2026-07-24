from database.weather_repository import insert_weather_event

# --------------------------------------------------------
# Dummy Weather Event
# --------------------------------------------------------

event = {
    "city": "Mumbai",
    "temperature_c": 28.5,
    "humidity_percent": 82,
    "wind_speed_kmh": 15.4,
    "pressure_hpa": 1008,
    "event_time": "2026-07-13 14:00:00",
    "producer_timestamp": "2026-07-13 14:01:05"
}

print("Testing Repository...")

insert_weather_event(event)

print("Repository Test Completed.")