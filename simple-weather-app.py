import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"☁️ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("❌ City not found or something went wrong.")

if __name__ == "__main__":
    API_KEY = "2c6c18e63cee661f35993a8a448ac882"
    city = input("Enter city name: ")
    get_weather(city, API_KEY)
