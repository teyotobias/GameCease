from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import Game, UserProfile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'company', 'description', 'year_released', 'price', 'cover']
    success_url = '/games/recommended'

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'games/signup.html'

class GameUpdate(UpdateView):
    model = Game
    fields = ['company', 'description', 'year_released']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

class GameDetail(DetailView):
    model = Game
    context_object_name = 'game'

class RecommendedGamesList(ListView):
    template_name = 'games/recommended_games.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.filter(recommended=True)


# def my_protected_view(request):
#     if not request.user.is_authenticated:
#         messages.add_message(request, messages.INFO, 'You must be logged in to view this page')
#         return redirect('login')
#     return render(request, 'games/recommended_games.html')
    

class NotRecommendedGamesList(ListView):
    template_name = 'games/not_recommended_games.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.filter(recommended=False, purchased=False)
    
@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    user_profile = UserProfile.objects.get(user=request.user)
    if game not in user_profile.games_in_cart.all():
        user_profile.games_in_cart.add(game)
        user_profile.total_cost += game.price
        user_profile.save()
        messages.success(request, "Game added to your cart!")
    else:
        messages.info(request, "This game is already in your cart")
    return redirect('display_cart')

@login_required
def remove_from_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    user_profile = UserProfile.objects.get(user=request.user)
    if game in user_profile.games_in_cart.all():
        user_profile.games_in_cart.remove(game)
        user_profile.total_cost -= game.price
        user_profile.save()
        messages.success(request, "Game removed from your cart!")
    else:
        messages.info(request, "This game is not in your cart")
    return redirect('display_cart')

@login_required
def display_cart(request):
    user_profile = UserProfile.objects.get(user=request.user)
    cart = user_profile.games_in_cart.all()
    total_cost = user_profile.total_cost
    context = {
        'cart': cart,
        'total_cost': total_cost,
    }
    return render(request, 'games/cart.html', context)

@login_required
def purchase(request):
    user_profile = UserProfile.objects.get(user=request.user)
    games_to_purchase = user_profile.games_in_cart.all()
    user_profile.purchased_games.add(*games_to_purchase)
    for game in games_to_purchase:
        game.purchased = True
        game.save()
    # user_profile.games_in_cart.clear()
    # user_profile.total_cost = 0
    user_profile.save()
    messages.success(request, "Thank you for your purchase! Your cart is now empty.")
    return redirect('thank_you')

@login_required
def thank_you(request):
    user_profile = UserProfile.objects.get(user=request.user)
    purchased_games = user_profile.games_in_cart.all()
    total_cost = user_profile.total_cost
    context = {
        'purchased_games': purchased_games,
        'total_cost': total_cost,
    }
    user_profile.games_in_cart.clear()
    user_profile.total_cost = 0
    user_profile.save()
    return render(request, 'games/thank_you.html', context)


def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


