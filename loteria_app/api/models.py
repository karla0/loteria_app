from django.db import models

import secrets
import string


def generate_game_code() -> int:
    """Generates a unique game code.
    
    Returns
    -------
        int
    - a unique 7 digit numerical code
    """
    while True:
        # code will only contain digits
        code_options = string.digits
        generated_game_code = ''.join(secrets.choice(code_options) for i in range(7))
        if Game.objects.filter(game_code=generated_game_code).count() == 0:
            break
    return int(generated_game_code)

def generate_player_id() -> string:
    """Generates a unique player id.
    
    Returns
    -------
        string
    - a unique 5 digit alphaneumeric code
    """
    while True:
        # code will have uppercase letters and numbers
        code_options = string.ascii_uppercase + string.digits
        generated_player_id = ''.join(secrets.choice(code_options) for i in range(5))
        if Player.objects.filter(player_id=generated_player_id).count() == 0:
            break
    return generated_player_id

# Create your models here.
class Game( models.Model):
    """ Model that describes a loteria game

    Attributes
    ----------
    cards_id : int
        ID given to card packs to be set in configuration file.
    
    created_at : DateTime
        when the game started

    host_id : int
        player of ID of whoever started the game, will control when game starts,
        what card deck is used and marker type.

    game_code : int
        code used to identify game when adding players. 

    marker_id : int
        ID given to the marker chosen for the game

    game_over : bool
        indicates when game has been won or if host indicates the 
        end to a game. 
        If True then game is over. 
    """
    # default 0 will just be regular loteria cards
    cards_id = models.IntegerField(null=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    game_code = models.IntegerField(null=False, default=generate_game_code, unique=True)
    host = models.CharField(max_length=100, unique=True)
    marker_id = models.IntegerField(null=True, default=1)
    game_over = models.BooleanField(null=True, default=True)
    

class Player(models.Model):
    """Model that describes a Player in the Game

    Attributes
    ----------

    name : string
        the name of the player
    wins : int
        the number of times this player has won
    losses : int
        the number of times this player has lost

    player_id : string
        the id assigned to a player during a game.
    
    currently_in_game : bool
        indicates whether player is currently in a game, 
        could be used in case of accidental tab close.
    """
    player_id = models.CharField(max_length=15, default=generate_player_id, unique=True)
    name = models.CharField(max_length=100, unique=False)
    wins = models.IntegerField(null=False, default=0)
    losses = models.IntegerField(null=False, default=0)
    currently_in_game = models.BooleanField(null=False, default=False)
