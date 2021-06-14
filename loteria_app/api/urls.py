from django.urls import path
from .views import GameView # main is url endpoint in views.py


# handles blank endpoint
# currently @ api/home
urlpatterns = [
    path('home', GameView.as_view())
]