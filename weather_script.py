import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather?q=santiago&appid=5ff8eacb04c4c82a5477ac8db4d313dc"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Failed to fetch data: {response.status_code}")
        return None

def display_weather_data():
    data = fetch_weather_data()
    if data:
        city_name.set(data.get("name", "N/A"))
        country.set(data.get("sys", {}).get("country", "N/A"))
        temperature.set(data.get("main", {}).get("temp", "N/A"))
        humidity.set(data.get("main", {}).get("humidity", "N/A"))
        wind_speed.set(data.get("wind", {}).get("speed", "N/A"))
        wind_deg.set(data.get("wind", {}).get("deg", "N/A"))
        cloudiness.set(data.get("clouds", {}).get("all", "N/A"))

app = tk.Tk()
app.title("Weather App")

city_name = tk.StringVar()
country = tk.StringVar()
temperature = tk.StringVar()
humidity = tk.StringVar()
wind_speed = tk.StringVar()
wind_deg = tk.StringVar()
cloudiness = tk.StringVar()

ttk.Label(app, text="City:").grid(column=0, row=0, sticky=tk.W)
ttk.Label(app, textvariable=city_name).grid(column=1, row=0, sticky=tk.W)

ttk.Label(app, text="Country:").grid(column=0, row=1, sticky=tk.W)
ttk.Label(app, textvariable=country).grid(column=1, row=1, sticky=tk.W)

ttk.Label(app, text="Temperature:").grid(column=0, row=2, sticky=tk.W)
ttk.Label(app, textvariable=temperature).grid(column=1, row=2, sticky=tk.W)

ttk.Label(app, text="Humidity:").grid(column=0, row=3, sticky=tk.W)
ttk.Label(app, textvariable=humidity).grid(column=1, row=3, sticky=tk.W)

ttk.Label(app, text="Wind Speed:").grid(column=0, row=4, sticky=tk.W)
ttk.Label(app, textvariable=wind_speed).grid(column=1, row=4, sticky=tk.W)

ttk.Label(app, text="Wind Degree:").grid(column=0, row=5, sticky=tk.W)
ttk.Label(app, textvariable=wind_deg).grid(column=1, row=5, sticky=tk.W)

ttk.Label(app, text="Cloudiness:").grid(column=0, row=6, sticky=tk.W)
ttk.Label(app, textvariable=cloudiness).grid(column=1, row=6, sticky=tk.W)

ttk.Button(app, text="Fetch Weather", command=display_weather_data).grid(column=0, row=7, columnspan=2)

app.mainloop()