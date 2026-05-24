import requests

pokemon = input("Enter pokemon name: ")

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(url)

data = response.json()

print("Name:", data["name"])
print("Height:", data["height"])
print("Weight:", data["weight"])
