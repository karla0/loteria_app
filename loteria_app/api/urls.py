from django.urls import path
from .views import CreatePlayerView, GameView, CreateGameView, PlayerView # main is url endpoint in views.py

urlpatterns = [
    path('view_games', GameView.as_view()),
    path('create_game', CreateGameView.as_view()),
    path('view_players', PlayerView._as_view()),
    path('create_player', CreatePlayerView.as_view())
]