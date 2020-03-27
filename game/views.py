from django.shortcuts import render

def game_list(request):
    return render(request, 'game/game_list.html', {})