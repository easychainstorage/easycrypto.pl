from django.contrib import admin
from .models import Glossary

# Register your models here.
@admin.register(Glossary)


class GlossaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'place_news')
    list_filter = ('place_news',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
