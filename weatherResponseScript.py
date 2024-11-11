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
    2000: ["2024-11-01 10:00:00", "2024-11-02 12:00:00", "2024-11-03 14:00:00"],
    2018: ["2024-11-04 09:00:00", "2024-11-05 16:00:00", "2024-11-06 18:00:00"],
    2020: ["2024-11-07 11:00:00", "2024-11-08 13:00:00", "2024-11-09 15:00:00"],
    2030: ["2024-11-01 10:00:00", "2024-11-02 12:00:00", "2024-11-03 14:00:00"],
    2050: ["2024-11-04 09:00:00", "2024-11-05 16:00:00", "2024-11-06 18:00:00"],
    2060: ["2024-11-07 11:00:00", "2024-11-08 13:00:00", "2024-11-09 15:00:00"],
    2100: ["2024-11-01 10:00:00", "2024-11-02 12:00:00", "2024-11-03 14:00:00"],
    2140: ["2024-11-04 09:00:00", "2024-11-05 16:00:00", "2024-11-06 18:00:00"],
    2170: ["2024-11-07 11:00:00", "2024-11-08 13:00:00", "2024-11-09 15:00:00"],
    2600: ["2024-11-01 10:00:00", "2024-11-02 12:00:00", "2024-11-03 14:00:00"],
    2610: ["2024-11-04 09:00:00", "2024-11-05 16:00:00", "2024-11-06 18:00:00"],
    2660: ["2024-11-07 11:00:00", "2024-11-08 13:00:00", "2024-11-09 15:00:00"]
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
