from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.sessions),
    re_path(r'(.+)/', views.sessions_for, name='movie_sessions')
]