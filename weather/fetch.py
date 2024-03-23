import requests
import json

origin_url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=ae0afb19484e68b62cdcb5c1f8691407"
response = requests.get(origin_url)
jsonResponse = json.loads(response.text)

temperature = int(jsonResponse["main"]["temp"] - 273.15)  
humidity = jsonResponse["main"]["humidity"]
feels_like = int(jsonResponse["main"]["feels_like"] -273.15)
main = jsonResponse["weather"][0]["main"]  
icon = jsonResponse["weather"]["icon"]
name = jsonResponse["name"]
print("Bölge:" ,name)
print("Sıcaklık:", temperature, "°C")
print("Nem Oranı:", humidity, "%")
print("Durumu:", main)
print("Hisedilen:" ,feels_like)
