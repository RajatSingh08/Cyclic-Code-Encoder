from django.urls import path
from . import views

urlpatterns = [
    path('', views.inputPage, name='input'),
    path('output/', views.outputPage, name='output'),
]
