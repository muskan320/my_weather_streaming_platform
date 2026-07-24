from database.weather_repository import get_latest_weather
def get_average_temperature():

    """
    Calculate average temperature
    across all districts.
    """

    records = get_latest_weather()

    if not records:

        return 0

    total_temperature = 0

    for record in records:

        total_temperature += record["temperature_c"]

    average_temperature = (
        total_temperature / len(records)
    )

    return round(average_temperature, 2)

def get_dashboard_summary():

    records = get_latest_weather()

    if not records:
        return None

    total_districts = len(records)

    average_temperature = (
        sum(record["temperature_c"] for record in records)
        / total_districts
    )

    average_humidity = (
        sum(record["humidity_percent"] for record in records)
        / total_districts
    )

    hottest = max(
        records,
        key=lambda record: record["temperature_c"]
    )

    coldest = min(
        records,
        key=lambda record: record["temperature_c"]
    )

    highest_wind = max(
        records,
        key=lambda record: record["wind_speed_kmh"]
    )

    return {

        "total_districts": total_districts,

        "average_temperature": round(
            average_temperature,
            2
        ),

        "average_humidity": round(
            average_humidity,
            2
        ),

        "hottest_district": hottest,

        "coldest_district": coldest,

        "highest_wind": highest_wind,

        "latest_weather": records

    }