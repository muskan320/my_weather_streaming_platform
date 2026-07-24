import streamlit as st
import plotly.express as px

from analytics.weather_analytics import (
    get_dashboard_summary
)
import streamlit as st

try:
    from streamlit_autorefresh import st_autorefresh
except Exception:
    # Fallback: use a simple HTML meta refresh if package isn't available
    import streamlit.components.v1 as components
    def st_autorefresh(interval: int, key: str = None):
        seconds = max(1, int(interval / 1000))
        components.html(f'<meta http-equiv="refresh" content="{seconds}">', height=0)

from analytics.weather_analytics import (
    get_dashboard_summary
)

st.set_page_config(

    page_title="Himachal Weather Dashboard",

    page_icon="🌦️",

    layout="wide"

)

st_autorefresh(

    interval=30 * 1000,

    key="weather_refresh"

)

st.set_page_config(
    page_title="Himachal Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Himachal Pradesh Weather Dashboard")
st.markdown("Real-Time Weather Streaming using Kafka")

summary = get_dashboard_summary()

if summary is None:

    st.warning("No Weather Data Available.")
    st.stop()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Average Temperature",
        f"{summary['average_temperature']} °C"
    )

with col2:

    st.metric(
        "Average Humidity",
        f"{summary['average_humidity']} %"
    )

with col3:

    st.metric(
        "Districts",
        summary["total_districts"]
    )

st.subheader("Latest Weather")

st.dataframe(
    summary["latest_weather"],
    use_container_width=True
)
st.subheader(
    "🌡 Temperature Comparison"
)

figure = px.bar(

    summary["latest_weather"],

    x="city",

    y="temperature_c",

    title="Temperature Across Himachal Districts"

)

st.plotly_chart(

    figure,

    use_container_width=True

)
st.markdown("---")
st.header("📊 Weather Analytics Dashboard")

weather_data = summary["latest_weather"]

# ===============================
# Row 1
# ===============================

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌡 Temperature by District")

    temp_fig = px.bar(
        weather_data,
        x="city",
        y="temperature_c",
        color="temperature_c",
        title="Temperature Comparison",
        labels={
            "city": "District",
            "temperature_c": "Temperature (°C)"
        }
    )

    st.plotly_chart(
        temp_fig,
        use_container_width=True
    )


with col2:

    st.subheader("💧 Humidity by District")

    humidity_fig = px.bar(
        weather_data,
        x="city",
        y="humidity_percent",
        color="humidity_percent",
        title="Humidity Comparison",
        labels={
            "city": "District",
            "humidity_percent": "Humidity (%)"
        }
    )

    st.plotly_chart(
        humidity_fig,
        use_container_width=True
    )

# ===============================
# Row 2
# ===============================

col3, col4 = st.columns(2)

with col3:

    st.subheader("💨 Wind Speed")

    wind_fig = px.bar(
        weather_data,
        x="city",
        y="wind_speed_kmh",
        color="wind_speed_kmh",
        title="Wind Speed Comparison",
        labels={
            "city": "District",
            "wind_speed_kmh": "Wind Speed (km/h)"
        }
    )

    st.plotly_chart(
        wind_fig,
        use_container_width=True
    )


with col4:

    st.subheader("🌍 Atmospheric Pressure")

    pressure_fig = px.bar(
        weather_data,
        x="city",
        y="pressure_hpa",
        color="pressure_hpa",
        title="Pressure Comparison",
        labels={
            "city": "District",
            "pressure_hpa": "Pressure (hPa)"
        }
    )

    st.plotly_chart(
        pressure_fig,
        use_container_width=True
    )

# ===============================
# Row 3
# ===============================

col5, col6 = st.columns(2)

with col5:

    st.subheader("🥧 Temperature Distribution")

    pie_fig = px.pie(
        weather_data,
        names="city",
        values="temperature_c",
        title="Contribution of Temperature"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )


with col6:

    st.subheader("📈 Temperature Ranking")

    sorted_weather = sorted(
        weather_data,
        key=lambda x: x["temperature_c"],
        reverse=True
    )

    rank_fig = px.bar(
        sorted_weather,
        x="temperature_c",
        y="city",
        orientation="h",
        color="temperature_c",
        title="District Temperature Ranking"
    )

    st.plotly_chart(
        rank_fig,
        use_container_width=True
    )

# ===============================
# Row 4
# ===============================

st.subheader("🌦 Complete Weather Table")

st.dataframe(
    weather_data,
    use_container_width=True,
    hide_index=True
)