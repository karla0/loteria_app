from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('game/<int:game_code>', index),
    path('player/<str:player_id>', index),
    path('join', index),
    path('start', index),
    path('waiting', index)
]
