def transform_weather_data(raw_data: dict) -> dict:
    """
    Transforme les données brutes de l'API météo
    en données simples et propres.
    """

    return {
        "city": raw_data.get("name"),
        "temperature": raw_data.get("main", {}).get("temp"),
        "humidity": raw_data.get("main", {}).get("humidity"),
        "description": raw_data.get("weather", [{}])[0].get("description"),
        "timestamp": raw_data.get("dt")
    }