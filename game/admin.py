from django.contrib import admin

from .models import Word, Category

class WordAdmin(admin.ModelAdmin):
    fields = ['category', 'word_text', 'pub_date', 'times_correct']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Word, WordAdmin)
admin.site.register(Category, CategoryAdmin)