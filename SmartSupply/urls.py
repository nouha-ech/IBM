"""
URL configuration for SmartSupply project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from main.views import form_view # import the form_view function
from main.views import provider_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path('form/', form_view, name='form_view'),  # connect the url to the form_view function
    path('provider/', provider_list, name='provider_list'),  #  for provider_list func
]
