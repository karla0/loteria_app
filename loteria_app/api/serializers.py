from rest_framework import serializers
from .models import Game, Player

class GameSerializer(serializers.ModelSerializer):
    """Deserializes game object retrieved from database."""
    class Meta:
        model = Game
        fields = ('id', 'game_code', 
                  'cards_id', 'host', 
                  'game_over', 'marker_id',
                  'created_at'
                  )

class CreateGameSerializer(serializers.ModelSerializer):
    """Class to serialize a game object for storing to database.
    
    Required Fields
    ---------------
    cards_id : int
    - the id of the theme of the card packs

    marker_id: int
    - the id of the kind of markers users selected
    """
    class Meta:
        model = Game
        fields = ('cards_id', 'marker_id')

class PlayerSerializer(serializers.ModelSerializer):
    """Deserializes player object retrieved from database"""
    class Meta:
        model = Player
        fields = ('id', 'player_id', 
                  'game_code',
                  'name', 'wins', 
                  'losses'
                  )

class CreatePlayerSerializer(serializers.ModelSerializer):
    """Class to serialize a player object for storing to database.
    
    Required Fields
    ---------------

    name : string
    the name the user wants displayed during the game.

    game_code : int
    the game code they are currently part of. Users may only be part of 1 game.
    """
    class Meta:
        model = Player 
        fields = ('name', 'game_code')
