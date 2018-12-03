from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('/output/', views.summariser, name='summariser'),
    path('', views.index, name='index'),
]
