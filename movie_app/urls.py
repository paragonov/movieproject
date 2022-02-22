from django.urls import path
from . import views


"""Конфигурация URLов приложение(movie_app)"""
urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
]