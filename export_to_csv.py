import psycopg2
import pandas as pd

# Connect to the database
conn = psycopg2.connect(dbname="weather_db", user="mousragheb")

# Query all weather data
df = pd.read_sql("SELECT * FROM weather ORDER BY timestamp DESC", conn)

# Export to CSV
df.to_csv("weather_data.csv", index=False)
print("Data exported to weather_data.csv")

conn.close()