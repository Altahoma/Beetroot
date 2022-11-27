import requests


url = "https://www.twitch.tv/robots.txt"

response = requests.get(url)
with open("robots.txt", "w") as file:
    file.write(response.text)
