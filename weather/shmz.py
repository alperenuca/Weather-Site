from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']  
        origin_url = f"http://api.openweathermap.org/data/2.5/weather?q={country}&APPID=ae0afb19484e68b62cdcb5c1f8691407"
        response = requests.get(origin_url)
        jsonResponse = json.loads(response.text)

        if response.status_code == 200:
            temperature = int(jsonResponse["main"]["temp"] - 273.15)  
            humidity = jsonResponse["main"]["humidity"]
            main = jsonResponse["weather"][0]["main"]  
            icon = jsonResponse["weather"][0]["icon"]
            feels_like = int(jsonResponse["main"]["feels_like"] -273.15)
            name = jsonResponse["name"]

            weather_data = {
                "temperature": temperature,
                "humidity": humidity,
                "main": main,
                "icon": icon,
                "feels_like": feels_like,
                "name":name
            }

            return render_template('index.html', weather=weather_data)
        else:
            error_message = f"Üzgünüz, {country} ait hava durumu bilgisi yok..."
            return render_template('index.html', error=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
