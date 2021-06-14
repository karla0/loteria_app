from django.shortcuts import render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
# Create your views here.

# api view give all game objects and use serializer
class GameView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

