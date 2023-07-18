from django.shortcuts import render, get_object_or_404
from .models import Glossary
from django.views import View
from news.views import post_search


class GlossaryPage(View):
    def get(self, request):
        if 'query' in request.GET:
            return post_search(request)
        GLOSSARY_FILTERS = (
            ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
            ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'),
            ('L', 'L'), ('M', 'M'), ('N', 'N'),
            ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'),
            ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z'))

        glossary = Glossary.object.all()
        glossary_alphabet = {}
        for char in GLOSSARY_FILTERS:
            glossary_alphabet.update({char[0]: glossary.filter(place_news=char[0])})

        return render(request,
                      'dictionary/dictionary.html', {'glossary': glossary_alphabet})
