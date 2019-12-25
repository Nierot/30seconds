from django.shortcuts import render
from django.http import HttpResponse, Http404
from game.utils import createWordList
from game.version import getVersion

"""
The view for rendering the game page
"""
def gameView(request):
    returnList = createWordList()
    version = getVersion()
    context = {'returnList' : returnList, 'version' : version}
    return render(request, 'game/words.html', context)

