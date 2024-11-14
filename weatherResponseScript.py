import json
import os
from datetime import datetime

# Maak een map voor weerdata als deze nog niet bestaat
os.makedirs('weather', exist_ok=True)

# Originele JSON response die als basis dient
original_json = {
    "zipCode": 2000,
    "coord": {"lon": 10.99, "lat": 44.34},
    "weather": [{"id": 501, "main": "Rain", "description": "moderate rain", "icon": "10d"}],
    "base": "stations",
    "main": {
        "temp": 298.48,
        "feels_like": 298.74,
        "temp_min": 297.56,
        "temp_max": 300.05,
        "pressure": 1015,
        "humidity": 64,
        "sea_level": 1015,
        "grnd_level": 933
    },
    "visibility": 10000,
    "wind": {"speed": 0.62, "deg": 349, "gust": 1.18},
    "rain": {"1h": 3.16},
    "clouds": {"all": 100},
    "dt": 1661870592,
    "sys": {
        "type": 2,
        "id": 2075663,
        "country": "IT",
        "sunrise": 1661834187,
        "sunset": 1661882248
    },
    "timezone": 7200,
    "id": 3163858,
    "name": "Zocca",
    "cod": 200
}

# Weersituaties volgens de weather API
weather_conditions = [
    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"},
    {"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"},
    {"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}
]

# Postcodes en bijbehorende tijdstippen voor ritten
stations = {
    2000: ["2020-02-01 18:25:59", "2020-02-01 21:58:37", "2020-03-07 16:12:47"],
    2018: ["2020-03-02 01:08:32", "2020-03-02 04:30:46", "2020-03-02 07:55:21"],
    2020: ["2020-03-07 16:03:43", "2020-03-02 01:34:03", "2020-03-02 08:37:25"],
    2030: ["2020-03-02 00:10:03", "2020-04-12 08:06:24", "2020-04-04 06:12:28"],
    2050: ["2019-09-22 08:36:14", "2019-09-22 10:55:15", "2019-09-22 16:49:38"],
    2060: ["2019-09-22 08:42:03", "2019-11-03 20:58:34", "2019-10-02 00:20:46"],
    2100: ["2019-10-02 08:47:25", "2019-11-03 20:15:59", "2019-12-02 06:20:35"],
    2140: ["2021-05-02 02:21:38", "2021-05-02 06:45:15", "2021-05-02 08:29:39"],
    2170: ["2022-07-02 07:15:09", "2022-07-02 15:46:30", "2022-07-03 10:52:55"],
    2600: ["2022-08-06 08:32:29", "2022-08-06 09:16:44", "2022-08-06 11:38:50"],
    2610: ["2023-09-11 07:55:02", "2023-09-11 09:27:42", "2023-09-11 10:05:21"],
    2660: ["2023-03-11 15:09:49", "2023-03-11 06:56:33", "2023-03-11 10:25:51"]
}


# Functie om een JSON response te genereren gebaseerd op de originele JSON
def generate_weather_response(zip_code, timestamp, condition):
    response = original_json.copy()

    # Wijzig alleen de velden die moeten worden aangepast
    response["zipCode"] = zip_code
    response["weather"] = [condition]
    response["dt"] = int(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").timestamp())

    return response


# JSON-bestanden genereren en opslaan
for zip_code, timestamps in stations.items():
    for i, timestamp in enumerate(timestamps):
        # Selecteer een weersituatie op basis van de index
        condition = weather_conditions[i]
        weather_data = generate_weather_response(zip_code, timestamp, condition)
        file_name = f"weather/{zip_code}_response_{i + 1}.json"

        # Sla het gegenereerde JSON-object op in een bestand
        with open(file_name, 'w') as json_file:
            json.dump(weather_data, json_file, indent=4)
        print(f"{file_name} aangemaakt.")

print("Alle weerdata JSON-bestanden zijn succesvol aangemaakt.")
