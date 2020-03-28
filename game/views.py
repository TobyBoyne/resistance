from django.shortcuts import render
from .models import GameInstance
from django.utils import timezone

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def game_list(request):
    games = GameInstance.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'game/game_list.html', {'games': games})