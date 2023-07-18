from django.db import models
from django.urls import reverse
from django_quill.fields import QuillField


class Glossary(models.Model):
    GLOSSARY_FILTERS = (
        ('A', 'A'), ('B', 'B'), ('C', 'C'),
        ('D', 'D'), ('E', 'E'), ('F', 'F'),
        ('G', 'G'), ('H', 'H'), ('I', 'I'),
        ('J', 'J'), ('K', 'K'),
        ('L', 'L'), ('M', 'M'), ('N', 'N'),
        ('O', 'O'), ('P', 'P'), ('Q', 'Q'),
        ('R', 'R'), ('S', 'S'), ('T', 'T'),
        ('U', 'U'), ('V', 'V'), ('W', 'W'),
        ('X', 'X'), ('Y', 'Y'), ('Z', 'Z'))

    LEVEL = (('basic', 'Podstawowy'), ('medium', 'Średniozaawansowany'), ('hard', 'Zaawansowany'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = QuillField(blank=True, null=True, default='')
    place_news = models.CharField(max_length=10,
                              choices=GLOSSARY_FILTERS,
                              default='A')
    level = models.CharField(max_length=20,
                              choices=LEVEL,
                              default='Podstawowy')
    object = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('slownik:slowik_detail',
                         args=[
                         self.slug])



