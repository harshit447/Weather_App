# Weather App
This is a simple weather app built using Python and Django that allows users to get current weather data for any location in the world. The app uses the OpenWeatherMap API to get weather data and displays the data on a web page.

# Prerequisites
To run the app, you will need the following installed on your machine:<br>

Python (version 3.8 or higher)<br>
Django (version 3.1 or higher)<br>
requests<br>
folium<br>
cachetools

# Getting Started

Clone the repository to your local machine using Git or download the ZIP file and extract it.<br>
Open a terminal or command prompt and navigate to the project directory.<br>
Run the following command to install the required packages:<br>
bash<br>
Copy code<br>
pip install -r requirements.txt<br>
Start the Django development server by running the following command:<br>
bash<br>
Copy code<br>
python manage.py runserver<br>
Open a web browser and go to http://127.0.0.1:8000/ to access the app.

# API Key
This application uses the OpenWeatherMap API to fetch weather data. To use this API, you need to obtain an API key from the OpenWeatherMap website. Once you have an API key, replace the YOUR_API_KEY_HERE placeholder in the scripts.js file with your actual API key.
const API_KEY = 'YOUR_API_KEY_HERE';

# Usage
To use the app, enter the name of a location (city or town) in the search box and click on the "Get Weather" button. The app will display the current temperature, humidity, wind speed, pressure, and weather conditions for the location, as well as a map showing the location.

# Credits
This project was created by Harshit Aneja. The application uses the following resources:

OpenWeatherMap API (https://openweathermap.org/)

