
from django.urls import path
from .views import weather

urlpatterns = [
    # Define a URL pattern for the weather view.
    path("", weather, name="weather"),
]
