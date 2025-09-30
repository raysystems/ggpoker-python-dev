
from app.modules.IPMAWebScraper import get_weather_forecast, parse_response
def getWeatherForeCast(req: dict ):
    awnser = get_weather_forecast(req['destrict'], req['city'])
    weather_data = parse_response(awnser)


    apireturn_data = {}
    if req['day'] == "all":
        apireturn_data = weather_data
    else:
        apireturn_data = awnser[req['day']]

    return {"status": "ok", "data": apireturn_data}