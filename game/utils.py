from game.models import Word, Category
import random
import math

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

def func_randomint(exp_parameter=3, root_parameter=1):
    """
    Returns random integer based on exponential or inverse quadratic relation (or both)
    such that proir less frequent words have higher probablity to appear

    times_appeared toevoegen enzo
    

    """
    sup = Word.objects.all().order_by("-id")[0].id - 1
    randfloat = random.uniform(0,sup)
    randint = math.floor(exp_parameter*(sup**(sup/randfloat)+1) + root_parameter(-1*math.sqrt(sup*randfloat)+sup)/2)
    return randint

def randomBoolean():
    """
    returns a random boolean
    """
    return random.randint(0,99) < 50

def catsStringToArray(catsString):
    """
    converts "[1,2,3]" to [1,2,3]
    """
    return list(map(int, catsString.strip('[]').split(',')))

def catsStringToStringArray(catsString):
    """
    converts '[1,2,3]' to ['joner1','joner2','Basic']
    """
    arr = catsStringToArray(catsString)
    returnlist = []
    for catid in arr:
        returnlist.append(Category.objects.get(id=catid).name)
    return returnlist


def specificWordList(catsString):
    """
    creates the full wordlist from selected categories
    """
    cats = catsStringToArray(catsString)
    wordList = []
    for i in cats:
        for word in Word.objects.all().filter(category=i):
            wordList.append(word)
    return wordList

def randomInt(catsString):
    """
    Returns a semi-random integer. Is based on how many times a word has appeared before
    """
    wordList = specificWordList(catsString)
    maximum = len(wordList) - 1
    half = round((xAppeared(">") - xAppeared("<")) / 2)
    while True:
        randID = random.randint(0,maximum)
        word = wordList[randID]
        if randomBoolean():
            return randID
        elif word.times_appeared < half:
            return randID


def createSpecificWordList(catsString):
    """
    Fetches all words, then returns 5 random ones to the view
    """
    wordList = specificWordList(catsString)
    returnList = []
    ids = []
    while len(ids) < 5:
        foo = randomInt(catsString)
        if len(ids) < 5:
            randInt = randomInt(catsString)
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