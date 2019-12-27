from django import forms
from .models import Word, Category
from game.utils import getBasicCategory

class WordForm(forms.Form):
    cats = Category.objects.all()
    word_text = forms.CharField(label='Word', max_length=30)
    selected_category = forms.ModelChoiceField(label='Category: ', queryset=cats, initial="Basic")
