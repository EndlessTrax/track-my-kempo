from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('training/', views.training_log, name='training-log'),
    path('register/', views.register, name='register'),
    path('training/new/', views.add_new_technique, name='new-technique'),
    path('training/technique/update/<int:id>', views.technique_update, name='update-technique'),
    path('training/technique/<int:id>', views.single_technique, name='single-technique'),
    path('training/technique/edit/<int:id>', views.edit_technique, name='edit-technique'),
    path('training/technique/delete/<int:id>', views.delete_technique, name='delete-technique'),
]