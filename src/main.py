#!/usr/bin/env python3
import os

choice = int(input('Enter\n1.City name\n2.Latitude & Longitude\n'))
if choice == 1:
    os.system('/home/shrinidhi/PycharmProjects/OpenWeatherAPI/src/city.py')
elif choice == 2:
    os.system('python3 /home/shrinidhi/PycharmProjects/OpenWeatherAPI/src/latlong.py')
else:
    print('Wrong choice')