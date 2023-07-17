from django.shortcuts import render

# Create your views here.
from .models import Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game

class GameCreate(CreateView):
    model = Game
    fields = ['title', 'company', 'description', 'year_released', 'price', 'cover']

class GameUpdate(UpdateView):
    model = Game
    fields = ['company', 'description', 'year_released']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

# class GameList(ListView):
#     model = Game
#     context_object_name = 'games'

class GameDetail(DetailView):
    model = Game
    context_object_name = 'game'

class RecommendedGamesList(ListView):
    template_name = 'games/recommended_games.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.filter(recommended=True)

class NotRecommendedGamesList(ListView):
    template_name = 'games/not_recommended_games.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.filter(recommended=False)
    
def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


