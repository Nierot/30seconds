from django.db import models
import random
from .randomname import randomNameTeam1, randomNameTeam2, randomGameName

class Category(models.Model):
    """
    Category model;  
    Attributes: name;  
    Functions: addCategory(cls, name), __str__()
    """ 
    name = models.CharField(max_length=200)
    def addCategory(cls, name):
        category = cls(name=name)
        category.save()
        return True
    def __str__(self):
        return self.name
    

class Word(models.Model):
    """
    Word model;  
    Attributes: category, word_text, pub_date, times_correct, times_appeared;  
    Functions: addWord(text, category), __str__()
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date created', auto_now_add=True)
    times_correct = models.IntegerField(default=0)
    times_appeared = models.IntegerField(default=0)
    def addWord(text, category):
        cat = Category.get_deferred_fields
        word = Word(word_text=text, category=category)
        word.save()
        return True
    def __str__(self):
        return self.word_text
    
class Game(models.Model):
    """
    Game model  
    Attributes: name, selected_categories,
    """
    name = models.CharField(max_length=20, default=randomGameName())
    selected_categories = models.CharField(max_length=500)
    team_name_one = models.CharField(max_length=20, default=randomNameTeam1())
    team_name_two = models.CharField(max_length=20, default=randomNameTeam2())
    date_created = models.DateTimeField('date created', auto_now_add=True)
    def setName(self, text):
        self.name = text
    def setCategory(self, categories):
        self.selected_categories = categories