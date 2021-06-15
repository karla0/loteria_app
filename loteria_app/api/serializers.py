from rest_framework import serializers
from .models import Game, Player

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_code', 'cards_id', 'host_id', 'game_over', 'marker_id','created_at')
    

class Player(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'player_id', 'name', 'wins', 'losses', 'currenty_in_game')
