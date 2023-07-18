from django.contrib import admin
from .models import Ebook, EbookEmails


@admin.register(Ebook)


class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'get_absolute_url',)
    list_filter = ('publish',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('-publish',)


@admin.register(EbookEmails)
class EbookEmailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'time')