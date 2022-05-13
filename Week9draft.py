from urllib import response
import requests
import json

api_key ='4542e18527933d8be01dc09fdc2693e6'

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=imperial"

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print("Temperature is " +
                   str(current_temperature)
                   + " degrees Fahrenheit")
else:
    print("City Not Found")
