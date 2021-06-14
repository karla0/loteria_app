from rest_framework import serializers
from .models import Game, Player

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'cards_id', 'host_id', 'marker_id', 'players','created_at')
    

class Player(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'wins', 'losses')
