from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('training/', views.training_log, name='training-log'),
    path('register/', views.register, name='register'),
]