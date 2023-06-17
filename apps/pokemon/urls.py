from django.urls import path
from . import views

urlpatterns = [
    path('pokemon_archivo/', views.pokemon_list, name='pokemon_archivo'),
]