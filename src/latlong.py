#!/usr/bin/env python3
import requests
import os

choice = int(input('Enter:\n1.Current location\n2.Some other location\n'))

if choice == 1:
    res = requests.get('http://ipinfo.io/')
    data = res.json()

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

elif choice == 2:
    latitude = input('Enter latitude: ')
    longitude = input('Enter longitude: ')

else:
    print('Wrong choice')

if choice == 1 or choice == 2:
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=a7b4d8bb5c172535c7bc4115a57c14f6&units=metric'.format(latitude, longitude)

    res = requests.get(url)
    data = res.json()

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
