import requests


api_key = "5cf81a0cb090af002983adb4a1af6052"
api_url = "https://api.openweathermap.org/data/2.5/forecast"
user_city = input("Enter your user_city: ")
params = {"q": user_city, "appid": api_key, "units": "metric"}

response = requests.get(url=api_url, params=params)
data = response.json()

if data["cod"] == "200":
    city = data["user_city"]["name"]
    country = data["user_city"]["country"]
    temperature = data["list"][0]["main"]["temp"]

    print(f"Temperature in {city}, {country}: {temperature}°C")
else:
    code = data["cod"]
    message = data["message"]

    print(f"Error: {code}, {message}")
