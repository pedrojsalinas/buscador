from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from buscador import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('buscador.urls')),
]
