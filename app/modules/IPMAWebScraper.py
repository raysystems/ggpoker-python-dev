
from bs4 import BeautifulSoup
import time
import tempfile
from app.cache.IPMACacheService import cacheIPMA
from app.cache.IPMACacheService import search_in_cache

from playwright.sync_api import sync_playwright

def get_weather_forecast(destrict, city):
    """
        Parses the HTML content to extract weather forecast data.

        Args:
            destrict - string: Destrict name
            city - string: City name

        Returns:
            string: Returns HTML of parsed page by playwright
    """
    destrict = destrict.replace(" ", "%20")
    city = city.replace(" ", "%20")
    if (search_in_cache(destrict, city)):
        cacheIPMAData = cacheIPMA[f"{destrict.lower()}_{city.lower()}"]
        return cacheIPMAData

    url_to_fetch = f"https://www.ipma.pt/pt/otempo/prev.localidade.hora/#{destrict}&{city}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url_to_fetch)
        html_content = page.content()
        browser.close()
    return html_content

def parse_response(html_content, destrict, city):
    """
        Parses the HTML content to extract weather forecast data.

        Args:
            html_content - string: HTML content of the weather forecast page.

        Returns:
            dict: A dictionary containing extracted weather data.
    """
    cache = search_in_cache(destrict, city)
    if (cache):
        print("cache hit ", cacheIPMA[f"{destrict.lower()}_{city.lower()}"]["data"])
        return cacheIPMA[f"{destrict.lower()}_{city.lower()}"]["data"]
    soup = BeautifulSoup(html_content, 'html.parser')
    # Get the weekly forecast div
    week_forecast = soup.find('div', id='weekly')

    weather = {}
    for day_div in week_forecast.find_all('div', class_='weekly-column'):

        # Date - div with class="date"

        date_div = day_div.find('div', class_='date')

        # get day number (Format returned: "Segunda, 1")
        day_number = date_div.get_text(strip=True).split(",")[-1].replace(" ", "")

        weather[day_number] = {} # init dict for the day
        weather[day_number]['date'] = date_div.get_text(strip=True)

        # Temperature (Min.) - class="tempMin"
        temp_min_div = day_div.find('span', class_='tempMin')
        weather[day_number]['temp_min'] = temp_min_div.get_text(strip=True)

        # Temperature (Max.) - class="tempMax"
        temp_max_div = day_div.find('span', class_='tempMax')
        weather[day_number]['temp_max'] = temp_max_div.get_text(strip=True)

        # Precipitation - class="precProb"
        prob_rain = day_div.find('div', class_='precProb')
        weather[day_number]['precipitation'] = prob_rain.get_text(strip=True)


    print(weather)
    if (not cache):
        cacheIPMA[f"{destrict.lower()}_{city.lower()}"] = {
            "data": weather,
            "ttl": time.time()
        }
    return weather

