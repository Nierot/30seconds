from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from game.utils import createWordList
from game.version import getVersion

from .models import Word, Category


def words(request):
    returnList = createWordList()
    return render(request, 'game/words.html', {'returnList': returnList})

def versionNumber(request):
    version = getVersion()
    print(version)
    return render(request, 'game/words.html', {'version': version})


def gameView(request):
    returnList = createWordList()
    version = versionNumber()
    context = {'returnList' : returnList, 'version' : version}
    return render(request, 'game/words.html', context)