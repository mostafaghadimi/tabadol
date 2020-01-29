from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from apps.books import views

urlpatterns = [
    path('', views.BooksList.as_view()),
    path('submit/', views.BookSubmit.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)