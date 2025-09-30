from fastapi import APIRouter
from app.controllers.weatherForecastController import getWeatherForeCast
router = APIRouter()


@router.get("/weatherForecast/{destrict}/{city}/{day}")
def get_weather_forecast(destrict: str, city: str, day: str):
    req = {
        "destrict": destrict,
        "city": city,
        "day": day
    }
    return getWeatherForeCast(req)