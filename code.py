import requests
import matplotlib.pyplot as plt

# API key and city name
api_key = "11b482b3f8c475a9eba18d93f959994b"
city = "Nagpur"

# API link
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

# getting data from API
response = requests.get(url)
data = response.json()

# checking if data is correct
if data["cod"] == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    print("Temperature:", temp)
    print("Humidity:", humidity)
    print("Pressure:", pressure)

    # graph
    labels = ["Temperature", "Humidity", "Pressure"]
    values = [temp, humidity, pressure]

    plt.bar(labels, values)
    plt.title("Weather Data Graph")
    plt.xlabel("Weather Parameters")
    plt.ylabel("Values")
    plt.show()

else:
    print("Error getting data from API")
