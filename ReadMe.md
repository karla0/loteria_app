# Loteria Game App

This app is based on the Mexican game of Loteria. 

## Gameplay:
- The game consists of a deck of 54 cards and a set of 4 x 4 game cards.
- Traditionally, there is a cantor/host who calls out the cards at a fast speed depending on how difficult the game should be.
- Players then get to choose from the set of game gards, people usually have their favorite but this game will render a random set everytime.
- Once the game starts, the cantor calls out the cards, if the player has a matching cell in their selected game card grid to the card called, the players place a marker on top to indicate a match.
- Markers are usually plastic dots, quarters or pinto beans.
- The first person to have a 100% matched grid, wins.

### Rules

1. Players are allowed to add markers after called card has passed.
2. Players with incorrectely marked cells will not be notified of the errors. 

# API Endpoints

## /create_game
    POST
    - takes card_id and marker_id
    - adds game to list of active games

## /view_games
    GET 
    - lists a every active game in the app pulled from sqlite3 database.
    
## /join
    - page for joining game, player must enter name.
## /start
    - page where host creates a game
    - user must select card theme and marker theme. 
    - Defaults to "Traditional" 
## /game
## /waiting