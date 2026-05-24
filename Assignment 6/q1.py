import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=91e1bd732de3c3db8a9c24f69ed4d3a8&units=metric"

    try:
       response = requests.get(url)
       response.raise_for_status()
       data = response.json()
       print("Temp: ",data['main']['temp'])
       print("Pressu",data['main']['pressure'])
       print("Sea level: ",data['main']['sea_level'])
       print("Ground level: ",data['main']['grnd_level'])
       print("humidity: ",data['main']['humidity'])
       print("Feels like: ",data['main']['feels_like'])
    
    except requests.exceptions.RequestException as e:
       print(e)

city = input("Enter city name: ")
weather_data(city)

