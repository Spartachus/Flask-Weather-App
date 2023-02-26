from flask import Flask,render_template,request,url_for
import requests
from dotenv import load_dotenv
import os

def configure():
  load_dotenv()

app = Flask(__name__)
 
@app.route('/', methods=['POST','GET'])  
def message():   
  configure()
  image_url = url_for('static', filename='css/cloud.png')
  if request.method == 'POST':    
    Api_Key = os.getenv("api_key") 
    try:

      city = request.form['contact']
      city = city.lower()

      loc_par = {"q":city,"appid": Api_Key,"limit":1}
      location = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=loc_par)
      data_location = location.json()
      lat = data_location[0]["lat"]
      lon = data_location[0]["lon"]
      country = data_location[0]["country"]

      parameters = {"lat": lat,"lon": lon,"appid": Api_Key,"units":"metric"}
      weather = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
      data_weather = weather.json()
      temperature = data_weather["main"]["temp"]
      country = data_weather["sys"]["country"]
      descripton = data_weather["weather"][0]["description"]
      shower = f"it currently feels like {temperature} celcius in {city},{country}\n Description: {descripton}"    
      return render_template("frosty.html",shower = shower,image_url = image_url) 
    except Exception:
      return render_template("failed.html",image_url = image_url)
  else:
    return render_template('index.html',image_url = image_url)  

if __name__ == '__main__':
    app.run(debug=True)

