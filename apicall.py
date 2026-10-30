import requests

def getWeatherData(latitude, longitude):
    # Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    response = requests.get(url)
    data = response.json()
    return data

weatherData = getWeatherData(48.8566, 2.3522)  # Coordinates for Paris

print(weatherData)
print(f"Current temperature in Paris: {weatherData['current']['temperature_2m']}°C")