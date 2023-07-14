from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #maps to view.home view function -> does not exist yet, create it
    path('about/', views.about, name='about'),
    path('games/', views.GameList.as_view(), name='games_index'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game_detail'), 
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    # path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),

]

