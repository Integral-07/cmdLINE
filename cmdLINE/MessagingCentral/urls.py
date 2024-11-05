from django.urls import path
from MessagingCentral import views

urlpatterns = [
    path('index/', views.index),
]