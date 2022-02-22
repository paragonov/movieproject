from django.shortcuts import render, get_object_or_404

from .models import Movie

""" Функция отображение всех фильмов """


def show_all_movie(request):
    movies = Movie.objects.order_by('name')
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })


""" Функция отображение информации одного фильма """


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movies.html', {
        'movie': movie
    })
