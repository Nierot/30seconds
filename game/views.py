from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
import random
from game.utils import kindaRandomInt

from .models import Word, Category


def index(request):
    wordList = Word.objects.all()
    returnList = []
    ids = kindaRandomInt()
    print(ids)
    i = 0 
    while i < 5:
        for i in ids:
            word = wordList[i]
            if word not in returnList:
                returnList.append(word)
                word.times_appeared += 1
                word.save()
                print(word)
                i += 1
    return render(request, 'game/words.html', {'returnList': returnList}) 
    """
    max = Word.objects.all().order_by("-id")[0].id - 1
    allWordsList = Word.objects.order_by('pub_date')
    wordList = []
    usedWords = []
    i = 0
    while i < 5:
        id = random.randint(0, max)
        if id not in usedWords:
            word = allWordsList[id]
            usedWords.append(id)
            wordList.append(word)
            word.times_appeared += 1
            wordList.append(word.times_appeared)
            word.save()
            i += 1
    """
