import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def fetch_weather(city: str, date: str):
    today = datetime.utcnow().date()
    target = datetime.strptime(date, "%Y-%m-%d").date()
    url = (
        "http://api.weatherapi.com/v1/history.json"
        if target < today else
        "http://api.weatherapi.com/v1/forecast.json"
    )

    params = {
        "key": API_KEY,
        "q": city,
        "dt": date,
        "days": 1,
    }

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

    forecast_day = data.get("forecast", {}).get("forecastday", [{}])[0]
    day = forecast_day.get("day", {})

    return {
        "city": city,
        "date": date,
        "max_temp": day.get("maxtemp_c", None),
        "min_temp": day.get("mintemp_c", None),
        "wind_kph": day.get("maxwind_kph", None),
        "condition": day.get("condition", {}).get("text", "")
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
