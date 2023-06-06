from django.urls import path
from . import views

urlpatterns = [
    path('catalog_archivo/', views.catalog_list, name='catalog_archivo'),
]