"""
URL configuration for recetas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recetas.views import home_views
from recetas.views import user_views

urlpatterns = [
    path('registro', user_views.registro, name='registro'),
    path('contacto', home_views.contacto, name='contacto'),
    path('', home_views.home, name='home'),
    path('admin/', admin.site.urls),
]