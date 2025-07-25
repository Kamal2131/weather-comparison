# --- weather/weather_fetcher.py ---
import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def fetch_weather(city: str, date: str):
    url = "http://api.weatherapi.com/v1/history.json"
    params = {"key": API_KEY, "q": city, "dt": date}

    try:
        r = requests.get(url, params=params)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(f"❌ Request failed for {city} on {date}: {e}")
        return None

    if "error" in data:
        print(f"❌ WeatherAPI Error: {data['error']['message']}")
        return None

    return {
        "city": city,
        "date": date,
        "max_temp": data["forecast"]["forecastday"][0]["day"]["maxtemp_c"],
        "min_temp": data["forecast"]["forecastday"][0]["day"]["mintemp_c"],
        "wind_kph": data["forecast"]["forecastday"][0]["day"]["maxwind_kph"],
        "condition": data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
    }


def get_weather_range(city, start_date, end_date):
    all_data = []
    date = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    while date <= end:
        data = fetch_weather(city, date.strftime("%Y-%m-%d"))
        if data:
            all_data.append(data)
        date += timedelta(days=1)
    return pd.DataFrame(all_data)