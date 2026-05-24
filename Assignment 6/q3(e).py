import requests

api_key = "XVGlq5DTANYzzpWfGbzRdeJH7nWNzW3OAqGQgFaX"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)

data = response.json()

print("Title:", data["title"])
print("Date:", data["date"])
print("Explanation:", data["explanation"])
print("Image URL:", data["url"])
