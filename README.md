# Weather Data Pipeline (Python)

## 📌 Project Overview

This project is a simple **Data Engineering pipeline** that collects weather data from an external API, processes the data, and stores it in a database.

The goal of this project is to demonstrate the basic components of a data pipeline:

- Data extraction from an API
- Data transformation and cleaning
- Data storage in a SQL database

This project was built as part of my learning journey into **Data Engineering**.

---

## ⚙️ Technologies Used

- Python
- REST API (OpenWeather)
- SQLite
- SQLAlchemy
- Git & GitHub

---

## 🏗️ Pipeline Architecture

The pipeline follows a simple Extract → Transform → Load (ETL) structure.
OpenWeather API
↓
api.py (Extract data)
↓
transform.py (Clean & structure data)
↓
database.py (Store data)
↓
SQLite database

---

## 📂 Project Structure
data-weather-project/
│
├── src/
│ ├── api.py # Fetch weather data from the API
│ ├── transform.py # Clean and structure the raw data
│ ├── database.py # Handle database connection and insertion
│ └── main.py # Orchestrates the pipeline
│
├── data/ # Stores database files
├── README.md
├── requirements.txt
└── .gitignore

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
git clone https://github.com/PixelNinja971/data-weather-project.git
cd data-weather-project

### 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Add your API key

Create a `.env` file in the root folder:
API_KEY=your_api_key_here

### 5️⃣ Run the pipeline
python src/main.py

---

## 📊 Example Output

When running the pipeline, the script fetches weather data and stores it in the SQLite database.

Example output:
Données sauvegardées :
{'city': 'Paris', 'temperature': 13.2, 'humidity': 59, 'description': 'nuageux'}

---

## 🎯 Learning Objectives

This project helped me understand:

- How to retrieve data from an API
- How to process JSON data
- How to structure a Python project
- How to store data in a SQL database
- How to manage a project with Git and GitHub

---

## 🚀 Possible Improvements

Future improvements for this project could include:

- Adding data validation checks
- Implementing logging
- Supporting multiple cities
- Scheduling the pipeline execution
- Deploying the pipeline in a cloud environment

---

## 👨‍💻 Author

Nathan  
Aspiring Data Engineer
