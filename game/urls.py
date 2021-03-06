from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:pk>/', views.game_page, name='game_page'),
    path('game/new/', views.new_game, name='new_game'),
]