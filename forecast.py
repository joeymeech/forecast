import requests
import json
from requests.exceptions import HTTPError

BASE_URL = 'https://api.weather.gov/'
PATH = 'points/'
print("This script gets the location and current weather of your entererd Latitude and Longitude coordinates")
print("(Using the weather.gov api) \n")
LAT = input("Enter your Latitude : ")
LONG = input("Enter your Longitude : ")


try:
    baseResponse = requests.get(f"{BASE_URL}{PATH}{LAT},{LONG}")
    baseResponse.raise_for_status()
    # access JSON content
    jsonResponse = json.loads(json.dumps(baseResponse.json()))

    # state and city names
    location = jsonResponse['properties']['relativeLocation']['properties']
    print("State: ", location['state'])
    print("City: ", location['city'])

    # gets the link to the actual weather
    newResponse = requests.get(jsonResponse['properties']['forecast'])
    newResponse.raise_for_status()
    jsonResponse = json.loads(json.dumps(newResponse.json()))

    detailedForecast = jsonResponse['properties']['periods'][0]['detailedForecast']
    print("Current weather: ", detailedForecast)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')