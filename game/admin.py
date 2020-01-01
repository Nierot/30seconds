from django.contrib import admin

from .models import Word, Category, Game

class WordAdmin(admin.ModelAdmin):
    fields = ['category', 'word_text']
    list_display = ['word_text', 'times_appeared', 'category']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

class GameAdmin(admin.ModelAdmin):
    fields= ['name', 'selected_categories', 'team_name_one', 'team_name_two']

admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)