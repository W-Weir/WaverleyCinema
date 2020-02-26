from django.shortcuts import render
from datetime import datetime, timezone
from Movies.models import Movie_Info, Session_Info

def get_movies():
    movies = Movie_Info.objects.all()
    return movies

def get_sessions():
    sessions = Session_Info.objects.all()
    return sessions

def now_playing(request):
    now_playing = get_movies()

    for i in now_playing:
        i.link = '/movies/' + i.title.lower().replace(' ','-')
        i.session_link = '/sessions/' + i.title.lower().replace(' ','-')

        today = datetime.now(timezone.utc)
        if today < i.date_ending and today > i.date_released:    
            i.status = 'Now Playing'
        elif today < i.date_released: 
            i.status = 'Coming Soon'
        else:
            i.status = 'Ended'

    context = {
        'movie_list': now_playing,
        'title':'Now Playing'
    }

    return render(request, 'Movies/movies.html', context)

def fuck(request):
    return render(request, 'Movies/fuck.html')

def movie_page(request, movie):
    context = {
        'movie':movie,
        'title':movie.title,
    }
    
    return render(request, 'Movies/movie.html', context)