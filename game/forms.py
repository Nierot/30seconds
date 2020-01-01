from django import forms
from .models import Word, Category
from .game import getBasicCategory

class WordForm(forms.Form):
    cats = Category.objects.all()
    word_text = forms.CharField(label='Word', max_length=30)
    selected_category = forms.ModelChoiceField(label='Category: ', queryset=cats, initial=Category.objects.get(id=15))

class NewGameForm(forms.Form):
    selected_categories = forms.ModelMultipleChoiceField(label='Categories', queryset=Category.objects.all())
    team_one_name = forms.CharField(label='Team 1', max_length=20)
    team_two_name = forms.CharField(label='Team 2', max_length=20)
