from . import views
from django.urls import path, include, re_path
from .models import Movie_Info

urlpatterns = [
    path('', views.now_playing),
    re_path(r'(.+)/$', views.movie_page)
]

