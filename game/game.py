from .models import Game, Category, Word
import datetime
import pytz

def getBasicCategory():
    """
    Returns the 'basic' category object
    """
    return Category.objects.all().get(id=3)

def getSelectedCategories(name):
    """
    Returns all selected categories
    """
    return Game.objects.get(name=name).selected_categories

def getID(name):
    return Game.objects.get(name=name).id

def makeBasic():
    '''
    adds words to the basic list
    '''
    wordlist = []
    cat = Category.objects.get(id=12)
    for word in wordlist:
        print(word)
        Word.addWord(word, cat)

def deleteOldGames():
    """
    deletes games that are older than 1 week
    """
    now = pytz.utc.localize(datetime.datetime.now())
    now = now.replace(tzinfo=pytz.utc)
    for game in Game.objects.all():
        if game.date_created < now-datetime.timedelta(hours=24):
            print("Deleted game: " +  game.name)
            game.delete()