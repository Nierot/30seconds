from .models import Word
import random

def xAppeared(operator):
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


def kindaRandomInt():
    max = Word.objects.all().order_by("-id")[0].id - 1
    returnList = []
    least = xAppeared(operator="<")
    most = xAppeared(operator=">")
    half = round((most - least) / 2)
    i = 0
    counter = 0
    while i < 5:
        randId = random.randint(0, max)
        word = Word.objects.all()[randId]
        if randId not in returnList:
            rareness = word.times_appeared
            print(rareness)
            print(half)
            if rareness <= half:
                returnList.append(randId)
                i += 1
            else:
                counter += 1
            if counter == 10:
                half += 1
                counter = 0
    return returnList