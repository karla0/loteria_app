from django.urls import path
from .views import GameView, CreateGameView # main is url endpoint in views.py


# handles blank endpoint
# currently @ api/home
urlpatterns = [
    path('view_games', GameView.as_view()),
    path('create_game', CreateGameView.as_view())
]