import requests,json
city = input("Enter the name of a city: ")
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city.lower().capitalize()}&APPID=213fc9be40420ed21ae1365c8dd63666&units=metric")
data = response.json()

print(f"Weather description of {city.lower().capitalize()}: {data['weather'][0]['description'].capitalize()}")
print(f"The temperature in {city.lower().capitalize()} is " + str(data['main']['temp']) + "°C")
print(f"The humidity in {city.lower().capitalize()} is {data['main']['humidity']}%")
print(f"The wind is blowing at a speed of {data['wind']['speed']} m/s")