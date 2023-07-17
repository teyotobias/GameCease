from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #login logout forms
    path('login/', auth_views.LoginView.as_view(template_name='games/login.html'), name='login'), #template form required for login. Sign up as well?
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  #no need to create template for this one. Redirects
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.home, name='home'), #maps to view.home view function -> does not exist yet, create it
    path('about/', views.about, name='about'),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='games_detail'), 
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/recommended/', views.RecommendedGamesList.as_view(), name='recommended_games'),
    path('games/not_recommended/', views.NotRecommendedGamesList.as_view(), name='not_recommended_games'),
    path('add_to_cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:game_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('purchase/', views.purchase, name='purchase'),
    path('cart/', views.display_cart, name='display_cart'),
    path('thank_you/', views.thank_you, name='thank_you'),

]


# path('endpoint/, grab_your_view, include_name')