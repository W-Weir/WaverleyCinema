from django.shortcuts import render
from Movies.models import Session_Info, Movie_Info

def get_sessions():
    sessions = Session_Info.objects.all()

    for i in sessions:
        i.booking_link = '/bookings/' + str(i.title).lower().replace(' ','-')

    return sessions

def sessions(request):
    all_sessions = get_sessions()

    context = {
        'sessions':all_sessions,
        'title':'Sessions'
    }

    return render(request, 'Sessions/sessions.html', context)

def get_movies():
    movies = Movie_Info.objects.all()
    return movies

def sessions_for(request, movie):
    title = movie.replace('-',' ').title()

    all_sessions = get_sessions()
    
    sessions = []
    for session in all_sessions:
        if title == session.title.title:    
            sessions.append(session)

    context = {
        'sessions':sessions,
        'title':movie.title,
    }

    return render(request, 'Sessions/test.html', context)
    