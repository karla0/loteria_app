from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Player
from .serializers import GameSerializer, CreateGameSerializer, PlayerSerializer, CreatePlayerSerializer
# Create your views here.

# api view give all game objects and use serializer
class GameView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CreateGameView(APIView):
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
    serializer_class = CreatePlayerSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')


