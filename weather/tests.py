from django.test import TestCase, RequestFactory
from unittest.mock import patch
from weather.views import weather, get_weather_from_openweathermap



class WeatherTest(TestCase):
    @patch("weather.views.requests.get")
    def test_get_weather_from_openweathermap(self, mock_get):
        """
        Test the `get_weather_from_openweathermap` function with both a valid and invalid location.
        """
        mock_data = {
            "main": {"temp": 283.57},
            "wind": {"speed": 3.3},
            "name": "London",
            "cod": 200,
        }
        mock_get.return_value.json.return_value = mock_data

        # Test with a valid location
        weather_data = get_weather_from_openweathermap("London")
        self.assertEqual(weather_data["name"], "London")
        self.assertEqual(weather_data["cod"], 200)
        self.assertEqual(weather_data["main"]["temp"]["celsius"], 10.42)
        self.assertEqual(weather_data["wind"]["speed"], 3.3)

        # Test with an invalid location
        weather_data = get_weather_from_openweathermap("InvalidLocation")
        self.assertEqual(weather_data, {})

    @patch("weather.views.get_weather_from_openweathermap")
    def test_weather_view(self, mock_weather_data):
        """
        Test the `weather` view function with both a GET and POST request, and with both valid and invalid data.
        """
        mock_weather_data.return_value = {
            "main": {"temp": {"kelvin": 283.57, "celsius": 10.42, "fahrenheit": 50.76}},
            "wind": {"speed": 3.3},
            "name": "London",
            "cod": 200,
        }
        request_factory = RequestFactory()

        # Test GET request
        request = request_factory.get("/weather")
        response = weather(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '"id_location"')

        # Test POST request with valid data
        request = request_factory.post("/weather", {"location": "London"})
        response = weather(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "London")
        self.assertContains(response, "10.42")
        self.assertContains(response, "3.3")
