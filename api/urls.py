# myapp/urls.py

from django.urls import path
from .views import YourDataView

urlpatterns = [
    # Define your API endpoint here
    path("api/your-endpoint/", YourDataView.as_view(), name="your-data"),
]
