import requests

city_name = input('Syötä paikkakunnan nimi: ')
limit = 1
api_key = "8bcf55516f5743dbda8b40b3a22d9ef7"
lang = "fi"

get_coordinates = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}"

try:
    coordinates = requests.get(get_coordinates)
    if coordinates.status_code == 200:
        coordinates = coordinates.json()
        for city in coordinates:
            lat = city['lat']
            lon = city['lon']

        get_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang={lang}'
        weather = requests.get(get_weather).json()
        print(f'{city_name.capitalize()}: {str(weather["weather"][0]["description"]).capitalize()}, lämpötila {round(weather["main"]["temp"])}°C.')

except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")