#!/usr/bin/env python3
import requests
import os

city = input('Enter your city: ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=a7b4d8bb5c172535c7bc4115a57c14f6&units=metric'.format(city)
res = requests.get(url)
data = res.json()
print(res)
print(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']

print('Temperature: {} degree celsius'.format(temp))
print('Wind speed: {} m/s'.format(wind_speed))
print('Latitude: {}'.format(latitude))
print('Longitude: {}'.format(longitude))
print('Description: {}'.format(description))
