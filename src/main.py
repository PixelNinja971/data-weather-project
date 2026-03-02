from api import get_weather

from transform import transform_weather_data
from database import init_db, insert_weather_data

if __name__ == "__main__":
    init_db()

    raw_data = get_weather("Paris")
    clean_data = transform_weather_data(raw_data)

    insert_weather_data(clean_data)

    print("Données sauvegardées :", clean_data)