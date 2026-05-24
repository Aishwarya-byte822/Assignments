import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd"

response = requests.get(url)

data = response.json()

print("Bitcoin:", data["bitcoin"]["usd"], "USD")
print("Ethereum:", data["ethereum"]["usd"], "USD")
print("Dogecoin:", data["dogecoin"]["usd"], "USD")
