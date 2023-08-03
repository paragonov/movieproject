from django.urls import path

from movie_app.views import show_all_movie, show_one_movie

urlpatterns = [
    path("", show_all_movie),
    path("movie/<slug:slug_movie>", show_one_movie, name="movie-detail"),
]
