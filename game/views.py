from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.edit import FormView

from game.utils import createWordList, getBasicCategory
from game.version import getVersion
from game.forms import WordForm
from game.models import Category, Word


def gameView(request):
    """
    The view for rendering the game page
    """
    returnList = createWordList()
    version = getVersion()
    context = {'returnList' : returnList, 'version' : version}
    return render(request, 'game/words.html', context)


def addWordsView(request):
    """
    The view for rendering the view to add words to the database
    """
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            Word.addWord(form.cleaned_data['word_text'], getBasicCategory())
            return HttpResponseRedirect('/game/')
    else:
        form = WordForm()
    return render(request, 'game/addWords.html', {'form': form})