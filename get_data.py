import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

### API call start
today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

### API call end

### Extracting daily data and creating a DataFrame

daily_data = data.get('daily', {})

df = pd.DataFrame({
    'date': daily_data.get('time', []),
    'max_temp': daily_data.get('temperature_2m_max', []),
    'min_temp': daily_data.get('temperature_2m_min', [])
})

df['date'] = pd.to_datetime(df['date'])

### Create a matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], label='Max Temp (°C)', color='red', marker='o')
plt.plot(df['date'], df['min_temp'], label='Min Temp (°C)', color='blue', marker='o')
plt.title('Paris Daily Max and Min Temperatures Over the Last Week')

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('paris_temperatures_last_week.png')
plt.show()

### Save the DataFrame to a CSV file

if not os.path.exists('data'):
    os.makedirs('data')
    
df.to_csv('data/paris_temperatures_last_week.csv', index=False)
print("Data saved to 'data/paris_temperatures_last_week.csv'")