from django.contrib import admin

from .models import Word, Category

class WordAdmin(admin.ModelAdmin):
    fields = ['category', 'word_text']
    list_display = ['word_text', 'times_appeared', 'category']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)