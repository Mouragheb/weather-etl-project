import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname="weather_db", user="mousragheb")
cur = conn.cursor()

# Query average temperature and humidity by city
cur.execute("""
    SELECT city, 
           ROUND(AVG(temp)::numeric, 2) AS avg_temp, 
           ROUND(AVG(humidity)::numeric, 2) AS avg_humidity 
    FROM weather 
    GROUP BY city
""")

rows = cur.fetchall()

# Print formatted report
print("\n=== Average Weather Data ===\n")
for row in rows:
    city, avg_temp, avg_humidity = row
    print(f"{city} — Temp: {avg_temp}°C | Humidity: {avg_humidity}%")

cur.close()
conn.close()