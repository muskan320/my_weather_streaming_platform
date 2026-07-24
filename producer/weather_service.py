"""
Weather Service

Responsibility:
Fetch weather data from Open-Meteo API
and create a weather event.
"""

import requests
from datetime import datetime


BASE_URL = "https://api.open-meteo.com/v1/forecast"


def build_weather_url(latitude, longitude):
    """
    Build Open-Meteo API URL
    """

    url = (
        f"{BASE_URL}"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,"
        f"relative_humidity_2m,"
        f"wind_speed_10m,"
        f"pressure_msl"
    )

    return url


def fetch_weather_data(latitude, longitude):
    """
    Fetch weather data from Open-Meteo API
    """

    print("=" * 60)
    print("Building Weather API URL...")

    url = build_weather_url(latitude, longitude)

    print(url)

    print("Calling Open-Meteo API...")

    response = requests.get(url)

    response.raise_for_status()

    print("Weather Data Received Successfully.")

    return response.json()


def create_weather_event(city, weather_data):
    """
    Convert API response into a weather event.
    """

    current = weather_data["current"]

    event = {

        "city": city,

        "temperature_c": current["temperature_2m"],

        "humidity_percent": current["relative_humidity_2m"],

        "wind_speed_kmh": current["wind_speed_10m"],

        "pressure_hpa": current["pressure_msl"],

        "event_time": current["time"],

        "producer_timestamp": datetime.now().isoformat()

    }

    return event


def get_weather_event(city, latitude, longitude):
    """
    Complete weather pipeline.

    1. Build URL
    2. Fetch Weather
    3. Create Weather Event
    4. Return Event
    """

    weather_data = fetch_weather_data(
        latitude,
        longitude
    )

    weather_event = create_weather_event(
        city,
        weather_data
    )

    return weather_event