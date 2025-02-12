from django.urls import path
from .views import usersIndex  # Importamos la vista

urlpatterns = [
    path('', usersIndex, name='users_index'),  # Definimos la URL de la vista
]
