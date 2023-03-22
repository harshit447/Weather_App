# Create your views here.

import requests
from django.shortcuts import render
from .forms import LocationForm
import logging
from cachetools.func import ttl_cache
import folium
from folium.plugins import MarkerCluster

logger = logging.getLogger()

@ttl_cache(maxsize=1024, ttl=10*60)
def get_weather_from_openweathermap(location):
    """
    This function get the weather from the openweathermap api
    :args:
        location: str (required)
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=8ebb8ab7af82c41e59c1233dda613a4e"
        response = requests.get(url)
        weather_data = response.json()
        temp_in_k = weather_data["main"]["temp"]
        # Converting kelvin to other temperatures
        weather_data["main"]["temp"] = {
            "kelvin": temp_in_k,
            "celsius": round(temp_in_k - 273.15, 2),
            "fahrenheit": round(((temp_in_k - 273.1) * (9 / 5)) + 32, 2),
        }
        lat = weather_data.get("coord", {}).get("lat")
        lon = weather_data.get("coord", {}).get("lon")
        # Check if the latitude and longitude coordinates are available
        if lat and lon:
            # Create a map using the latitude and longitude coordinates
            map = folium.Map(location=[lat, lon], zoom_start=12)
            # Add a marker for the location
            marker = folium.Marker(location=[lat, lon])
            marker.add_to(map)
            # Generate the HTML for the map
            map_html = map._repr_html_()
        print(weather_data)
        return weather_data
    except Exception:
        return {}


def weather(request):
    """ 
    A view function that handles a user's request to get weather data for a specified location.
    
    Parameters:
    ----------
    request : HttpRequest object
        Represents the request that the user made to the server.
    
    Returns:
    -------
    HttpResponse object
        Represents the response to the user's request. If the user made a POST request with a valid location,
        the response will include weather data for that location. Otherwise, the response will include a
        form for the user to enter a location.
    """
    if request.method == "POST":
        # If the user made a POST request, validate the form data.
        form = LocationForm(request.POST)
        if form.is_valid():
            # If the form data is valid, extract the location and get weather data for that location.
            location = form.cleaned_data["location"]
            
            return render(
                request,
                "weather.html",
                {"weather_data": get_weather_from_openweathermap(location)
                 
                 },
            )
    else:
        # If the user did not make a POST request, display a form for the user to enter a location.
        form = LocationForm()
    return render(request, "index.html", {"form": form})
