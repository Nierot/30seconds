from django.contrib import admin

from .models import Word, Maker

class WordAdmin(admin.ModelAdmin):
    fields = ['maker', 'word_text', 'pub_date', 'times_correct']

class MakerAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Word, WordAdmin)
admin.site.register(Maker, MakerAdmin)