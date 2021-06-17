from django.db import models

import secrets
import string

CARD_PACK_CHOICES = (
    ('1', 'Traditional Cards'),
    ('2', 'Special Cards'),
    ('3', 'Other Themed Cards')
)

MARKER_CHOICES = (
    ('1', 'Plastic Dots'),
    ('2', 'Quarters'),
    ('3', 'Beans')
)

def generate_game_code() -> int:
    """ Generates a unique game code.
    
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

    Fields
    ------
    cards_id : int
    - the id of the card theme chosen by user during creation of game.

    created_at : dateTime
    - the time that the game was started.

    game_code : int
    - a unique 7 digit code assigned during creation 
    needed to join games.

    host : string
    - the session key of the person who started the game
    ensures that users do not have more that 1 running game.

    game_over : bool
    - defaults to True for now but will default to False upon creation.

    maker_id : int
    - the id of the marker type chosen by user during creation of game.

    Notes
    -----
    - Considering making game_code primary key instead
    """
    # default 0 will just be regular loteria cards
    # TODO cards_id and marker_id should be choices not harded coded values
    game_code = models.IntegerField(null=False, default=generate_game_code, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100, unique=True)
    cards_id = models.CharField(max_length=10, choices=CARD_PACK_CHOICES, default='1')
    marker_id = models.CharField(max_length=10, choices=MARKER_CHOICES, default='1')
    game_over = models.BooleanField(null=True, default=True)
    

class Player(models.Model):
    """ Model that describes a Player in the Game

    Attributes
    ----------

    name : string
        the display name of the player.
    wins : int
        the number of times this player has won.
    losses : int
        the number of times this player has lost.
    player_id : string
        the id assigned to a player during a game.
    game_code : int
        the game code of the game joined, will be null if no game has been joined.
    """
    player_id = models.CharField(max_length=15, default=generate_player_id, unique=True)
    game_code = models.IntegerField(null=True)
    name = models.CharField(max_length=100, unique=False)
    wins = models.IntegerField(null=False, default=0)
    losses = models.IntegerField(null=False, default=0)


 