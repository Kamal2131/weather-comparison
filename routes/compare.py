from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.s3_utils import list_weather_keys, read_df_from_s3, save_df_to_s3
from weather.weather_fetcher import get_weather_range

router = APIRouter()

templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")


def get_stats(city, start, end):
    key = f"{city}_{start}_{end}.csv"
    df = read_df_from_s3(key)

    if df is None or df.empty or "max_temp" not in df.columns:
        df = get_weather_range(city, start, end)
        if df.empty or "max_temp" not in df.columns:
            print(f"❌ No weather data for {city} from {start} to {end}")
            return None
        save_df_to_s3(df, key)

    return {
        "name": city.title(),
        "max": round(df["max_temp"].mean(), 1),
        "min": round(df["min_temp"].mean(), 1),
        "wind": round(df["wind_kph"].mean(), 1),
        "rain": df[df["condition"].str.contains("rain", case=False)].shape[0],
    }

@router.post("/compare", response_class=HTMLResponse)
async def compare_weather(
    request: Request,
    city1: str = Form(None),
    city2: str = Form(None),
    start: str = Form(None),
    end: str = Form(None),
    selected_key1: str = Form(None),
    selected_key2: str = Form(None)
):
    # If using dropdown selection
    if selected_key1 and selected_key2:
        df1 = read_df_from_s3(selected_key1)
        df2 = read_df_from_s3(selected_key2)

        if df1 is None or df2 is None:
            return templates.TemplateResponse("weather.html", {
                "request": request,
                "city1": None,
                "city2": None,
                "error": "One or both historical datasets are missing or corrupted."
            })

        stats1 = {
            "name": selected_key1.split("_")[0].title(),
            "max": round(df1["max_temp"].mean(), 1),
            "min": round(df1["min_temp"].mean(), 1),
            "wind": round(df1["wind_kph"].mean(), 1),
            "rain": df1[df1["condition"].str.contains("rain", case=False)].shape[0]
        }

        stats2 = {
            "name": selected_key2.split("_")[0].title(),
            "max": round(df2["max_temp"].mean(), 1),
            "min": round(df2["min_temp"].mean(), 1),
            "wind": round(df2["wind_kph"].mean(), 1),
            "rain": df2[df2["condition"].str.contains("rain", case=False)].shape[0]
        }

        return templates.TemplateResponse("weather.html", {
            "request": request,
            "city1": stats1,
            "city2": stats2,
            "all_keys": list_weather_keys()
        })

    # Otherwise: handle live form request
    stats1 = get_stats(city1, start, end)
    stats2 = get_stats(city2, start, end)

    return templates.TemplateResponse("weather.html", {
        "request": request,
        "city1": stats1,
        "city2": stats2,
        "all_keys": list_weather_keys()
    })