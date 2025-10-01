
from app.modules.IPMAWebScraper import get_weather_forecast, parse_response
def getWeatherForeCast(req: dict ):
    awnser = get_weather_forecast(req['destrict'], req['city'])
    weather_data = parse_response(awnser, req['destrict'], req['city'])


    apireturn_data = {}
    if req['day'] == "all":
        apireturn_data = weather_data
    else:
        if req['day'] not in weather_data:
            return {"status": "error", "message": f"Day is not available in IPMA. Only Days - (" + ", ".join(weather_data.keys()) + " )"}
        apireturn_data = weather_data[req['day']]

    return {"status": "ok", "data": apireturn_data}