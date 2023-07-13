from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

#setup for index view
def games_index(request):
    return render(request, 'games/index.html')
    # videogames = Game.objects.all()
    # return render(request, 'games/index.html', {
    #     'games': videogames
    # })

# setup for details view
def games_detail(request):    #need game_id in parameters as well
    return render(request, 'games/detail.html')
    # requestedGame = Game.objects.get(id=game_id)
    # return render(request, 'games/detail.html', {
    #     'game': requestedGame
    # })
