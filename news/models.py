from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_quill.fields import QuillField
from django_resized import ResizedImageField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                self).get_queryset()\
                .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    PLACE_CHOICE = (
        ('main_news', 'Main News'),
        ('es_1', 'Easy News 1'),
        ('an_1', 'Inne 1'),
    )

    CATEGORY_CHOICE = (
        ('kryptowaluty', 'kryptowaluty'),
        ('nauka', 'nauka'),
        ('analiza', 'analiza'),
        ('metaverse', 'metaverse'),
        ('NFT', 'NFT'),
        ('regulacje', 'regulacje'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='news_posts')
    body_v1 = QuillField(blank=True, null=True, default='')
    reklama = models.IntegerField(default=3)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    place_news = models.CharField(max_length=10,
                              choices=PLACE_CHOICE,
                              default='Main News')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    tag = models.CharField(max_length=250,
                           default='#crypto')
    image = ResizedImageField(force_format="WEBP", quality=75, upload_to='images')

    category = models.CharField(max_length=50,
                              choices=CATEGORY_CHOICE,
                              default='')
    object = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('news:post_detail',
                         args=[self.category,
                         self.slug])

    def get_absolute_category(self):
        return reverse('news:post_category',
                       args=[self.category])

    def get_absolute_link(self):
        return reverse('news:post_category',
                       args=[self.category])

