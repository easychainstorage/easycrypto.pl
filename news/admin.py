from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe


@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status', 'tag', 'place_news', 'get_absolute_url', 'category')
    list_filter = ('status', 'created', 'publish', 'author', 'category')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', '-publish')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        # ex. the name of column is "image"
        obj = '/media/motywacja.jpg'
        if obj:
            return mark_safe('<h1>Systematyczność tworzy prace Easy</h1>'
                             '<img src="{0}" style="width:500px;height:auto" />'.format(obj))
        else:
            return '(No image)'

    image_preview.short_description = 'Dawka motywacji'

