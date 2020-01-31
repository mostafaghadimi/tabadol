from django.contrib import admin
from django.urls import path, include
from .views import UserList

urlpatterns = [
    path('', UserList.as_view()),
]
