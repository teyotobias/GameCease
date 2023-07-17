from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #maps to view.home view function -> does not exist yet, create it
    path('about/', views.about, name='about'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='games_detail'), 
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/recommended/', views.RecommendedGamesList.as_view(), name='recommended_games'),
    path('games/not_recommended/', views.NotRecommendedGamesList.as_view(), name='not_recommended_games'),
]


# path('endpoint/, grab_your_view, include_name')