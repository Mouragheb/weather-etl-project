import schedule
import time
from weather_etl import fetch_weather, store_weather, CITIES

def run_etl():
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            store_weather(data)
            print(f"Stored weather for {city}")

schedule.every().day.at("08:00").do(run_etl)

print("Scheduler started. Waiting to run at 08:00 daily...")
while True:
    schedule.run_pending()
    time.sleep(60)