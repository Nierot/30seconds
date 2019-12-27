from .models import Word, Category
import random

def getBasicCategory():
    """
    Returns the 'basic' category object
    """
    return Category.objects.all().get(id=2)


def xAppeared(operator):
    """
    Returns the least/most amount of times a word has appeared
    """
    foo = Word.objects.all()
    least = 1000
    most = 0
    if operator == "<":
        for i in foo:
            if i.times_appeared < least:
                least = i.times_appeared
        return least
    else:
        for i in foo:
            if i.times_appeared > most:
                most = i.times_appeared
        return most


def randomBoolean():
    """
    returns a random boolean
    """
    return random.randint(0,99) < 50


def randomInt():
    """
    Returns a semi-random integer. Is based on how many times a word has appeared before
    """
    wordList = Word.objects.all()
    max = Word.objects.all().order_by("-id")[0].id - 1
    half = round((xAppeared(">") - xAppeared("<")) / 2)
    while True:
        randID = random.randint(0,max)
        word = wordList[randID]
        if randomBoolean():
            return randID
        elif word.times_appeared < half:
            return randID


def createWordList():
    """
    Fetches all words, then returns 5 random ones to the view
    """
    wordList = Word.objects.all()
    returnList = []
    ids = []
    while len(ids) < 5:
        foo = randomInt()
        if len(ids) < 5:
            randInt = randomInt()
            if randInt not in ids:
                ids.append(randInt)
    i = 0
    while i < 5:
        for j in ids:
            word = wordList[j]
            if word not in returnList:
                returnList.append(word)
                word.times_appeared += 1
                word.save()
                i += 1
    return returnList

#Not in use anymore, still has problems with being stuck in a loop
def kindaRandomInt():
    max = Word.objects.all().order_by("-id")[0].id - 1
    returnList = []
    least = xAppeared(operator="<")
    most = xAppeared(operator=">")
    half = round((most - least) / 2)
    i = 0
    counter = 0
    while len(returnList) != 5:
        randId = random.randint(0, max)
        if randId not in returnList:
            randFactor = random.randint(0, 100)
            if randFactor < 50:
                returnList.append(randId)
            else:
                j = 0
                while j != 1:
                    randId = random.randint(0, max)
                    word = Word.objects.all()[randId]
                    rareness = word.times_appeared
                    if rareness <= half:
                        returnList.append(randId)
                        j = 1
                    else:
                        counter += 1
                    if counter == 10:
                        half += 1
                        counter = 0
    return returnList