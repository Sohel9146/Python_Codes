import requests

API_KEY = "7d5c321c0f818732e35ca97329121a15"

City_Name = input("Enter City Name : ")

URL =  f"https://api.openweathermap.org/data/2.5/weather?q={City_Name}&appid={API_KEY}"

response = requests.get(URL)

if response.status_code == 200:
        weather_data = response.json()
        weather = weather_data['weather'][0]['description']
        temp = weather_data['main'] ['temp'] -273.15
        
        print(f"Weather In {City_Name} : {round(temp,2)} °C with : {weather}")
else:
        print(f"Invalid City Name : {City_Name}")
