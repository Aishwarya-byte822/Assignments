# NEWS

import requests

api_key = "7feb433527094035a548ce162414642a"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)

data = response.json()

articles = data["articles"]

for news in articles:
    print(news["title"])











