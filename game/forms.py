from django import forms
from .models import Word, Category
from .game import getBasicCategory

class WordForm(forms.Form):
    cats = Category.objects.all()
    word_text = forms.CharField(label='Word', max_length=30)
    selected_category = forms.ModelChoiceField(label='Category: ', queryset=cats, initial="Niels")

class NewGameForm(forms.Form):
    selected_categories = forms.ModelMultipleChoiceField(label='Category: ', queryset=Category.objects.all(), initial="Niels")
    team_one_name = forms.CharField(label='Team 1', max_length=20)
    team_two_name = forms.CharField(label='Team 2', max_length=20)
