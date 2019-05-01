from django.urls import path
from buscador import views

urlpatterns = [
    path('buscar/', views.BuscadorView.as_view()),
]
