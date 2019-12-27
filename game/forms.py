from django import forms
from .models import Word, Category

class WordForm(forms.Form):
    word_text = forms.CharField(label='Word', max_length=30)