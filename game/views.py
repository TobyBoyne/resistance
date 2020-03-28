from django.shortcuts import render, get_object_or_404
from .models import GameInstance
from django.utils import timezone


def game_list(request):
    games = GameInstance.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'game/game_list.html', {'games': games})

def game_page(request, pk):
    game = get_object_or_404(GameInstance, pk=pk)
    return render(request, 'game/game_page.html', {'game':game})