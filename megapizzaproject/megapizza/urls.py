from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('corf/', views.corf, name='corf'),
]