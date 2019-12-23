from django.shortcuts import render
import random
from django.http import HttpResponse, Http404

from .models import Word, Maker


def index(request):
    max = Word.objects.all().order_by("-id")[0].id - 1
    allWordsList = Word.objects.order_by('pub_date')
    wordList = []
    usedWords = []
    i = 0
    while i < 5:
        id = random.randint(0, max)
        if id not in usedWords:
            usedWords.append(id)
            wordList.append(allWordsList[id])
            i += 1
    output = ', '.join([foo.word_text for foo in wordList])
    return HttpResponse(output)