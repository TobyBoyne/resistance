from django.shortcuts import render, get_object_or_404, redirect
from .models import GameInstance
from .forms import NewGameForm
from django.utils import timezone

from game_logic.main import GameHandler


def game_list(request):
    games = GameInstance.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'game/game_list.html', {'games': games})

def game_page(request, pk):
    game = get_object_or_404(GameInstance, pk=pk)
    game_handler = GameHandler()
    game.text = game_handler.play()
    return render(request, 'game/game_page.html', {'game':game})

def new_game(request):
    if request.method == "POST":
        form = NewGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.author = request.user
            game.published_date = timezone.now()
            game.save()
            return redirect('game_page', pk=game.pk)
    else:
        form = NewGameForm()
    return render(request, 'game/new_game.html', {'form': form})