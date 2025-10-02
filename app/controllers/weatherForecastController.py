from fastapi.responses import JSONResponse
from app.modules.IPMAWebScraper import get_weather_forecast, parse_response
def getWeatherForeCast(req: dict ):
    awnser = get_weather_forecast(req['destrict'], req['city'])
    weather_data = parse_response(awnser, req['destrict'], req['city'])

    if req['day'] == "all":
        return JSONResponse(status_code=200, content={"status": "ok", "data": weather_data})

    else:
        if req['day'] not in weather_data:
            return JSONResponse(
                status_code=404,
                content={
                    "status": "error",
                    "message": f"Day is not available in IPMA web, Only Days - (" + ", ".join(weather_data.keys()) + " )"
                }
            )

        return JSONResponse(status_code=200, content={"status": "ok", "data": weather_data[req['day']]})