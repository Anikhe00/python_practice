import requests

# OpenWeatherMap API key
API_KEY = "f745bbdc0d98c29ca408d7b40471e5d6"

# Get city name from user input
city = input("Enter city name: ")

# API endpoint URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# Make API request and save the response
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
else:
    print(f"Failed to fetch weather data. Status code: {response.status_code}")
    exit(1)

# Extract relevant weather information
country = data["sys"]["country"]

weather = data["weather"][0]["main"]
weather_description = ""

# Map weather condition to a description
if weather == "Clouds":
  weather_description = "Cloudy"
elif weather == "Clear":
  weather_description = "Clear"
elif weather == "Rain":
  weather_description = "Rainy"
elif weather == "Snow":
  weather_description = "Snowy"
else:
  weather_description = "Unknown"


temp = data["main"]["temp"]
temp_in_celsius = round(temp - 273.15)

humidity = data["main"]["humidity"]

wind = data["wind"]["speed"]

# Print the weather report
print("==== Weather Report ====")
print(f"{city.capitalize()}, {country}")
print(f"Current weather: {weather_description}")
print(f"Temperature: {temp_in_celsius}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind}km/h")
