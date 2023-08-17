from django.shortcuts import render
import requests
from django.urls import path
from django.http import JsonResponse
from . import views
#requesting acces to our html file
def my_view(request):
    return render(
        request, 
        "index.html")
#creating our url
urlpatterns = [
    path('weather/', views.weather_view, name='weather'),
]
#implementing our api
def weather_view(request): 
    city_value = request.GET.get('city', 'VARANASI')
    api_key= "2f745fa85d563da5adb87b6cd4b81caf"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_value}&appid={api_key}&units=metric"
#server-side api
    try: 
        response = requests.get(url)
        data = response.json()
        context = {
            'data': data, 
        }
    except requests.exceptions.RequestException as e: 
        context = {
            'error': 'City not found',
        }
    return render(request, 'index.html', context)    
