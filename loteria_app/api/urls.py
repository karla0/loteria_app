from django.urls import path
from .views import CreatePlayerView, GameView, CreateGameView, GetGame, GetPlayer, PlayerView # main is url endpoint in views.py

urlpatterns = [
    path('view-games', GameView.as_view()),
    path('view-players', PlayerView.as_view()),
    path('create-game', CreateGameView.as_view()),
    path('create-player', CreatePlayerView.as_view()),
    path('get-game', GetGame.as_view()),
    path('get-player', GetPlayer.as_view())
]