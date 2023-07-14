from django.shortcuts import render

# Create your views here.
from .models import Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = ['company', 'description', 'year_released']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

class GameList(ListView):
    model = Game
    context_object_name = 'games'

class GameDetail(DetailView):
    model = Game
    context_object_name = 'game'

def home(request):

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


