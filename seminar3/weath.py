import requests
import json

def get_weather_data(city_name, api_key):
   url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru"
   response = requests.get(url)
   if response.status_code == 200:
      data = response.json()
   return {
         'temperature': data['main']['temp'],
         'description': data['weather'][0]['description'],
         'pressure': data['main']['pressure'],
         'humidity': data['main']['humidity']
   }
   

# Ваш API ключ от OpenWeatherMap
api_key = '309c9ca6fb4036e41902e90d0ad350b0'

# Список городов для запроса
cities = ['Minsk', 'Moscow', 'Kyiv', 'Warsaw']

# Словарь для хранения данных о погоде
weather_data = {}

# Получение данных о погоде для каждого города
for city in cities:
   city_weather = get_weather_data(city, api_key)
   if city_weather:
      weather_data[city] = city_weather

# Сохранение структурированных данных в файл JSON
with open('weather_data.json', 'w', encoding='utf-8') as f:
   json.dump(weather_data, f, ensure_ascii=False, indent=4)
   print("Данные о погоде для выбранных городов успешно сохранены в файл 'weather_data.json'.")
   
