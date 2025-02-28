from django.urls import path
from .views import lista_eventos, lista_boletos

urlpatterns = [
    path('eventos/', lista_eventos, name='lista_eventos'),
    path('boletos/', lista_boletos, name='lista_boletos'),
]