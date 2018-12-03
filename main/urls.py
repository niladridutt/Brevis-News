from django.urls import path
from . import views


urlpatterns = [
    path('output/', views.summariser, name='summariser'),
    path('', views.index, name='index'),
]
