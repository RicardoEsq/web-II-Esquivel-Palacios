from django.shortcuts import render  # Importamos render para mostrar HTML
from .models import User  # Importamos el modelo User para obtener los datos

def usersIndex(request):
    users = User.objects.all()  # Recupera todos los usuarios de la base de datos
    return render(request, 'users/index.html', {'users': users})  # Envía los datos a la plantilla
