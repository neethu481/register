"""BookRegister URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from book_register import views


urlpatterns = [
    path('', views.book_form, name='book_insert'),  # get and post req. for insert operation
    path('<int:id>/', views.book_form, name='book_update'),  # get and post req. for update operation
    path('delete/<int:id>/', views.book_delete, name='book_delete'),
    path('list/', views.book_list, name='book_list'),


]






