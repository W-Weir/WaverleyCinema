from django.shortcuts import render

def get_sessions():
    import datetime
    from Movies.models import Session_Info

    today = datetime.date.today()

    sessions = []
    today_sessions = Session_Info.objects.all()

    for session in today_sessions:
        if session.date == today:
            sessions.append(session)

    return sessions

def today(request):
    sessions = get_sessions()

    context = {
        'sessions':sessions,
        'title':'Today',
    }

    return render(request, 'Today/today.html', context)

