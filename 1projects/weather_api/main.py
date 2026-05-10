# CLI Weather App
# A terminal app that fetches real-time weather.
# used OpenWeatherMap API
# error handling invalid city,no internet
# using separate modules name api.py,main.py
# Upgrade it:
# Cache results locally (avoid repeated API calls)
# Add unit conversion (Celsius/Fahrenheit)
# API key eb1e43412af9c1e2de5b0cde0114e9ed
# /data/2.5/weather -->free
# geocoding API: to convert city names directly in coordinates
import api


def main():
    print("Welcome to Get Weather App: ")
    api_key = "eb1e43412af9c1e2de5b0cde0114e9ed"

    # Getting coordinates of city
    x, y, city = api.get_coordinate(api_key)
    print(f"lat: {x}\n" f"longt: {y}")

    # Getting weather
    weather_cond, temp, feels_like, humidity = api.get_weather(api_key, x, y)

    # printing output
    print(
        f"====Weather report of {city}:====\n"
        f"    Weather: {weather_cond}\n"
        f"    Temperature: {kelvin_celsius(temp)}°C\n"
        f"    Feels Like: {kelvin_celsius(feels_like)}°C\n"
        f"    Humidity: {humidity}%\n"
        "================================="
    )


def kelvin_celsius(s):
    return round(float(s) - 273.15, 1)


main()
