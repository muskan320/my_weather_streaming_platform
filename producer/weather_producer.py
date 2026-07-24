"""
Weather Producer

Responsibility:
1. Fetch weather for all districts
2. Publish each weather event to Kafka
3. Repeat every 30 seconds
"""

import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
import time
import logging

from configs.districts import HIMACHAL_DISTRICTS

from producer.weather_service import get_weather_event

from producer.kafka_producer import (
    publish_and_confirm,
    close,
)


def run_weather_producer():

    print("Weather Producer Started")

    while True:

        print("=" * 70)
        print("Fetching Weather For All Districts")
        print("=" * 70)

        for district in HIMACHAL_DISTRICTS:

            try:

                city = district["city"]
                latitude = district["latitude"]
                longitude = district["longitude"]

                print(f"\nFetching Weather For : {city}")

                event = get_weather_event(
                    city,
                    latitude,
                    longitude
                )

                print("Weather Event Created")

                print(event)

                metadata = publish_and_confirm(
                    event,
                    key=city
                )

                logging.info(
                    f"""
Weather Published Successfully

City      : {city}
Topic     : {metadata.topic}
Partition : {metadata.partition}
Offset    : {metadata.offset}
"""
                )

            except Exception as e:

                logging.exception(
                    f"Error Processing {district['city']} : {e}"
                )

        print("\nCompleted One Complete Weather Cycle")
        print("Waiting 30 Seconds...\n")

        time.sleep(30)


if __name__ == "__main__":

    try:

        run_weather_producer()

    except KeyboardInterrupt:

        logging.info(
            "Producer Stopped By User."
        )

    finally:

        close()