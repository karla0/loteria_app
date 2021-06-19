from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Player
from .serializers import GameSerializer, CreateGameSerializer, PlayerSerializer, CreatePlayerSerializer
# Create your views here.

class GameView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayerView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CreateGameView(APIView):
    """
    Used by endpoint to create a new game 
    and stores to database using serializer
    

    Returns
    -------

        Response
        -  takes data passed in from request and creates a 
    """
    serializer_class = CreateGameSerializer
    def post(self, request, format=None):
        # checks for existing session if not create a session key
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        # checks if data attempting to be passed in is matching to serializer fields
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cards_id = serializer.data.get('cards_id')
            marker_id = serializer.data.get('marker_id')
            host = self.request.session.session_key
            # checks if other games contain same session key dont really need now.
            queryset = Game.objects.filter(host=host)
            if queryset.exists():
                # ensures host doesn't have many game rooms open
                game = queryset[0]
                game.cards_id = cards_id
                game.marker_id = marker_id
                game.save(update_fields=['cards_id', 'marker_id'])
                return Response(GameSerializer(game).data, status=status.HTTP_200_OK)
            else:
                game = Game(host=host, cards_id=cards_id, marker_id=marker_id)
                game.save()
                return Response(GameSerializer(game).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)


class CreatePlayerView(APIView):
    """Creates a player from name and game code."""
    serializer_class = CreatePlayerSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        if serializer.is_valid():
            name = serializer.data.get('name')
            game_code = serializer.data.get('game_code')
            host_key = self.request.session.session_key
            queryset = Player.objects.filter(host_key= host_key)
            if queryset.exists():
                player = queryset[0]
                player.name = name
                player.game_code = game_code
                player.save(update_fields=['name', 'game_code'])
                return Response(PlayerSerializer(player).data, status=status.HTTP_200_OK)
            else:
                player = Player(host_key= host_key, name=name, game_code=game_code)
                player.save()
                return Response(PlayerSerializer(player).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)


class GetGame(APIView):
    """
    Retrives game with matching code from database 
    and sets is_host by matching session keys.

    Returns
    -------
        Response
        - HTTP 200 OK - game was retrieved sucessfully
        - HTTP 400 Bad Request - Game Not Found - Game code does not match any existing games - 
        no matching player found with that id
        - HTTP 400 Bad Request - Invalid Data - the data type or format is not valid.
    
    """
    serializer_class = GameSerializer
    lookup_url_params = 'game_code'

    def get(self, request, format=None):
        game_code = request.GET.get(self.lookup_url_params)
        if game_code != None:
            game = Game.objects.filter(game_code=game_code)
            if len(game) > 0:
                data = GameSerializer(game[0]).data
                data['is_host'] = self.request.session.session_key == game[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Game Not Found': 'Code does not match any games. Check code.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Bad Request': 'Invalid Data' }, status=status.HTTP_400_BAD_REQUEST)

class GetPlayer(APIView):
    """
    Takes player id parameter and returns matching player info
    from database.

    Returns
    -------
        Response
        - HTTP 200 OK - player was retrieved sucessfully
        - HTTP 400 Bad Request - Player Not Found - 
        no matching player found with that id
        - HTTP 400 Bad Request - Invaid Data - the data type or format is not valid.
    """
    serializer_class = PlayerSerializer
    lookup_url_parameters = 'player_id'

    def get(self, request, format=None):
        player_id = request.GET.get(self.lookup_url_parameters)
        if player_id != None:
            player = Player.objects.filter(player_id=player_id)
            if len(player) > 0:
                data = PlayerSerializer(player[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({"Player Not Found": "No player to display."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Bad Request': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)


