from django.db import models


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

    marker_id : int
        ID given to the marker chosen for the game

    players : List
        For now a list of players that are part of the game 
    """
    # default 0 will just be regular loteria cards
    cards_id = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    host_id = models.IntegerField(null=False, default=0)
    marker_id = models.IntegerField(null=False, default=0)
    players = models.IntegerField(null=False, default=0)
    

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
    """
    # id is automatically given by django
    name = models.CharField(max_length=100, null=False, unique=False)
    wins = models.IntegerField(null=False, default=0)
    losses = models.IntegerField(null=False, default=0)
