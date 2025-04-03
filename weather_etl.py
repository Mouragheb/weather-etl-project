import requests
import psycopg2
from datetime import datetime

API_KEY = "f7dafaa4ae80dacaaf40bf0c9c315117"
CITIES = ["Houston", "New York", "Los Angeles", "Chicago"]
DB_NAME = "weather_db"
USER = "mousragheb"  # Change this to your Mac username if needed

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Error handling: If 'main' is not in the response, print error and skip this city
    if "main" not in data:
        print(f"Error fetching data for {city}: {data}")
        return None

    return {
        "city": city,
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "timestamp": datetime.utcnow()
    }

def store_weather(data):
    conn = psycopg2.connect(dbname=DB_NAME, user=USER)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id SERIAL PRIMARY KEY,
            city TEXT,
            temp REAL,
            humidity INTEGER,
            timestamp TIMESTAMP
        )
    """)
    cur.execute("""
        INSERT INTO weather (city, temp, humidity, timestamp)
        VALUES (%s, %s, %s, %s)
    """, (data["city"], data["temp"], data["humidity"], data["timestamp"]))
    conn.commit()
    cur.close()
    conn.close()

for city in CITIES:
    weather = fetch_weather(city)
    if weather:  # Only store if fetch_weather returned valid data
        store_weather(weather)
        print(f"Stored weather for {city}")