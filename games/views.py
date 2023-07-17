from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib import messages
from .models import Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'company', 'description', 'year_released', 'price', 'cover']

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
        return Game.objects.filter(recommended=False)
    
def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


