from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse

from .utils import createSpecificWordList
from .randomname import randomGameName
from .game import *
from .version import getVersion
from .forms import WordForm, NewGameForm
from .models import Category, Word, Game

def gameView(request):
    return HttpResponseRedirect('/game/basic')

def gameSpecificView(request, name):
    version = getVersion()
    returnList = createSpecificWordList(getSelectedCategories(name))
    teamname = 'oof'
    context = {'returnList' : returnList, 'version' : version, 'teamname': teamname}
    return render(request, 'game/words.html', context)

def addWordsView(request):
    """
    The view for rendering the view to add words to the database
    """
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            cat =  form.cleaned_data['selected_category']
            Word.addWord(form.cleaned_data['word_text'], cat)
            return HttpResponseRedirect('/addWords/')
    else:
        form = WordForm()
    return render(request, 'game/addWords.html', {'form': form})

def indexView(request):
    """
    The view for rendering the index page
    """
    #version
    version = getVersion()

    #select category

    if request.method =='POST':
        form = NewGameForm(request.POST)
        if form.is_valid():
            #categories
            cats = []
            cat = form.cleaned_data['selected_categories']
            for foo in cat:
                cats.append(foo.id)

            #names
            teamone = form.cleaned_data['team_one_name']
            teamtwo = form.cleaned_data['team_two_name']

            #new game
            name=randomGameName()
            game = Game(name=name,team_name_one=teamone,team_name_two=teamtwo,selected_categories=cats)
            game.save()
            return redirect('beforeGameView', name=name)
    else:
        form = NewGameForm()
    return render(request, 'game/index.html', {'version': version, 'form': form})

def beforeGameView(request, name):
    version = getVersion()
    game = Game.objects.get(name=name)
    teamone = game.team_name_one
    teamtwo = game.team_name_two
    context = {'version': version, 'teamone': teamone, 'teamtwo':teamtwo, 'name': name}
    return render(request, 'game/beforeGame.html', context)