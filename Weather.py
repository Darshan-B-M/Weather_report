import requests
from datetime import datetime

# My OpenWeatherMap API key
user_api="d29be881535d2d1137f95668143e4ce6"
location =input("Enter City Name-->")

# To get api link:  https://openweathermap.org/current#other
complete_api_link=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

# Fetch the weather data from the API
api_link=requests.get(complete_api_link)
api_data =api_link.json()

# Check if the city is valid
if api_data['cod']=='404':
    print("Invalid City Please enter correctly..!")
else:
    # Extract data from the API response

    kelvin_temp = api_data['main']['temp']
    celsius_temp = kelvin_temp - 273.15           #convert Fahrenheit to celsius

    description=api_data['weather'][0]['description']
    humidity=api_data['main']['humidity']
    wind_speed=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %y | %I:%M:%S %p" )

    # Display the weather information
    print("---------------------------------------------------------")
    print("Weather Statistics for {} on {}".format(location.upper(),date_time))
    print("---------------------------------------------------------")

    print("Current Temperature is: {:.2f} deg c".format(celsius_temp))
    print("Current Weather Description :",description)
    print("Current Humidity : ",humidity,"%")
    print("Current Wind Speed : ",wind_speed,"kmph\n")
    print("Thank You...!")