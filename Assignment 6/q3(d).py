import requests

base_currency = input("Enter base currency: ").upper()
target_currency = input("Enter target currency: ").upper()
amount = float(input("Enter amount: "))

api_key = "5a0abcbaa0cae06af3e3f8ac"

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

response = requests.get(url)

data = response.json()

rate = data["conversion_rates"][target_currency]

converted_amount = amount * rate

print(f"{amount} {base_currency} = {converted_amount} {target_currency}")
