from sqlalchemy import create_engine, Table, Column, String, Float, Integer, MetaData

engine = create_engine("sqlite:///data/weather.db")
metadata = MetaData()

weather_table = Table(
    "weather",
    metadata,
    Column("city", String),
    Column("temperature", Float),
    Column("humidity", Integer),
    Column("description", String),
    Column("timestamp", Integer),
)

def init_db():
    metadata.create_all(engine)

def insert_weather_data(data: dict):
    with engine.connect() as conn:
        conn.execute(weather_table.insert().values(**data))