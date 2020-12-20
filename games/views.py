from django.shortcuts import render
from . models import Game


def game_view(request):
    games = Game.objects.all()
    return  render(request, "game_view.html", {'games':games})
