from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #maps to view.home view function -> does not exist yet, create it
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:finch_id>/', views.games_detail, name='detail')
]

