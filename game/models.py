from django.db import models

class Maker(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Word(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')
    times_correct = models.IntegerField(default=0)
    def __str__(self):
        return self.word_text
    