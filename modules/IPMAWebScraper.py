from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def get_weather_forecast(destrict, city):
    """
        Gets the weather forecast for a given district and city using Selenium packd. .

        Args:
            destrict (str): Name of the district or island
            city (str): Name of the city or town

        Returns:
            str: HTML content of the weather forecast page.
    """
    destrict = destrict.replace(" ", "%20")
    city = city.replace(" ", "%20")

    url_to_fetch = f"https://www.ipma.pt/pt/otempo/prev.localidade.hora/#{destrict}&{city}"

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url_to_fetch)


    html_content = driver.page_source
    driver.quit()
    return html_content

def parse_response(html_content):
    """
        Parses the HTML content to extract weather forecast data.

        Args:
            html_content (str): HTML content of the weather forecast page.

        Returns:
            dict: A dictionary containing extracted weather data.
    """

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


    #print(weather)
    return weather

#response = get_weather_forecast("Madeira", "Funchal")
#parse_response(response)