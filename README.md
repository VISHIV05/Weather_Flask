# 🌦️ Weather Flask

A simple Flask-based web application that fetches real-time weather data from the OpenWeatherMap API and provides it in multiple formats — JSON, CSV, Excel, and XML. Easily configurable and extendable, ideal for learning REST APIs, file conversion, and basic Flask routing.


## 🚀 Features

* Fetch real-time weather data for any city
* Convert and export weather data in:

  * JSON (default)
  * CSV
  * Excel (XLSX)
  * XML
* Modular structure with separate modules for fetching, processing, and converting data
* Clean and simple Flask API endpoints

---

## 📁 Project Structure

```
weather_flask/
│
├── app.py                # Main Flask app
├── fetch_data.py         # Fetch data from OpenWeatherMap API
├── process_data.py       # Clean and extract relevant data
├── convert_data.py       # Convert data to CSV, Excel, and XML
├── config.py             # Configuration file (API key, default city, etc.)
├── templates/            # HTML templates (if needed)
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/weather_flask.git
   cd weather_flask
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key and configuration:**

   * Edit `config.py` with your OpenWeatherMap API key and optionally set a default city.

   ```python
   API_KEY = 'your_api_key_here'
   CITY = 'Mumbai'  # Default city
   ```

4. **Run the Flask app:**

   ```bash
   python app.py
   ```

---

## 🌐 API Endpoints

| Endpoint                          | Method | Description                              |
| --------------------------------- | ------ | ---------------------------------------- |
| `/get_weather_data?city=CityName` | GET    | Fetches and returns weather data in JSON |
| `/download_csv?city=CityName`     | GET    | Downloads weather data as a CSV file     |
| `/download_excel?city=CityName`   | GET    | Downloads weather data as an Excel file  |
| `/download_xml?city=CityName`     | GET    | Downloads weather data as an XML file    |

> 🔍 Replace `CityName` with your desired location.

---

## 🧪 Example

**Request:**

```
GET /get_weather_data?city=Delhi
```

**Response:**

```json
{
  "city": "Delhi",
  "temperature": "34°C",
  "humidity": "56%",
  "description": "Clear sky"
}
```

---

## 🛠 Tech Stack

* Python 3.x
* Flask
* Requests
* Pandas
* xml.etree.ElementTree

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

* [OpenWeatherMap API](https://openweathermap.org/api) — for providing weather data
* Flask documentation — [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

---

