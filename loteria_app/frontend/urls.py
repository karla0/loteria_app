from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('game/<int:gameCode>', index),
    path('join', index),
    path('start', index),
    path('waiting', index)
]
