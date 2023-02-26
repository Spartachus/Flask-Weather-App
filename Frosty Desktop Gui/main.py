from tkinter import *
from ttkbootstrap import *
import requests
from tkinter import messagebox
from dotenv import load_dotenv
import os
import pyperclip

def configure():
  load_dotenv()

#----------------------------------------------*Api Processing*----------------------------------------------#

def api():
    configure()
    try:
        city = city_entry.get()
        Api_Key = os.getenv("api_key") 
        loc_par = {"q":city,"appid": Api_Key,"limit":1}
        
        location = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=loc_par)
        data_location = location.json()
        lat = data_location[0]["lat"]
        lon = data_location[0]["lon"]
        country = data_location[0]["country"]
        print(f"These are you cordinates latitude: {lat} ,longtitude: {lon}")


        parameters = {"lat": lat,"lon": lon,"appid": Api_Key,"units":"metric"}
        weather = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
        data_weather = weather.json()
        temperature = data_weather["main"]["temp"]
        country = data_weather["sys"]["country"]
        weather = data_weather["weather"][0]["icon"]
        weather_label.config(text=f"it currently feels like {int(temperature)}° celcius in {city},{country}")
        messagebox.showinfo(title = "Tip", message = "Check out the Website:\nhttp://spartachus345.pythonanywhere.com")
        pyperclip.copy("http://spartachus345.pythonanywhere.com")
    except Exception:
        messagebox.showinfo(title="Error",message = "Enter A valid city name!!")



#---------------------------------------------* Ui Configuration *-------------------------------------------#
window = Window(themename="darkly")
window.title("Frosty")
window.geometry("480x550")

canvas = Canvas(width=200, height = 200)
logo_img = PhotoImage(file= "cloud.png")

canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0,column = 1, columnspan=3,padx=150,pady=50)

#---------------------------------------------* Button And Entries Configuration *-------------------------------------------#

city_entry = Entry(width = 30)
weather_button = Button(text ="Search",command=api)
weather_label = Label(text ="The weather Gui",font = "Calibri 18")
logo_label = Label(text="Frosty.io",font = "Calibri 12")

city_entry.grid(row = 3,column = 1,columnspan=3)
weather_label.grid(row = 2,column = 1,columnspan=3)
weather_button.grid(row = 3,column = 3)
logo_label.grid(row=1,column=1,columnspan=3)

window.mainloop()
api()