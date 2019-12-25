from django.db import models
import random

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created', auto_now_add=True)
    times_correct = models.IntegerField(default=0)
    times_appeared = models.IntegerField(default=0)
    def addWord(text):
        word = Word(word_text=text)
        return word
    def __str__(self):
        return self.word_text
    