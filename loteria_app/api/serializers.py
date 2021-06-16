from rest_framework import serializers
from .models import Game, Player

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_code', 
                  'cards_id', 'host', 
                  'game_over', 'marker_id',
                  'created_at'
                  )

class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('cards_id', 'marker_id')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'player_id', 
                  'name', 'wins', 
                  'losses', 'currenty_in_game'
                  )

class CreatePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player 
        fields = ('name')
