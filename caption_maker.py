import requests
import creds

def weather_caption():
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=berlin&appid={creds.weather}")
    temp = r.json()['main']['temp'] - 273.15
    return int(temp)


def feeling():
    if weather_caption() > 18:
        return "warm"
    elif weather_caption() < 13:
        return "cold"
    else:
        return "comfortable"
