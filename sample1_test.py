import requests
 
def get_weather(city):
    response = requests.get(f"https://api.weather.example/{city}", timeout=10)
    response.raise_for_status()
    return response.json()
 
 
get_weather("London")
