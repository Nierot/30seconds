from .models import Game, Category, Word

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
