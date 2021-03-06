"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from calculator.views import get_expression, list_of_expressions, detail_of_expression, delete_expression

urlpatterns = [
    path('', get_expression, name='index'),
    path('database', list_of_expressions, name='database'),
    path('database/<int:id>/', detail_of_expression, name='details'),
    path('database/<int:id>/delete/', delete_expression, name='delete')
]
