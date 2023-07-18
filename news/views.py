from django.views import View
from .models import Post
from django.shortcuts import render, get_object_or_404, get_list_or_404
import re
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm


def post_search(request):
    query = None
    results = []
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Post.object.annotate(search=SearchVector('title')).filter(search=query)
    return render(request,
                  'search/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        if 'query' in request.GET:
            return post_search(request)
        posts = Post.published.all()
        main_news = posts.filter(place_news='main_news').order_by('-publish')[0]
        easy_news = posts.filter(place_news='es_1').order_by('-publish').all()[:2]
        other_news = posts.order_by('-publish').all()
        other = []
        for news in other_news:
            if news != main_news:
                if news not in easy_news:
                    other.append(news)
        video2 = 'https://www.youtube.com/watch?v=aTXcT1EtRjA'
        video1 = 'https://www.youtube.com/embed/69HLn9qDSwQ'
        video3 = 'https://www.youtube.com/shorts/xoHmEHwFivQ'
        return render(request,
                      'news/home.html',
                      {'main_news': main_news,
                        'easy_news': easy_news,
                        'other_news': other[:9],
                        'video1': video1,
                        'video2': video2,
                        'video3': video3})


class NewsDetail(View):
    def get(self, request, category, post):
        if 'query' in request.GET:
            return post_search(request)
        post = get_object_or_404(Post, slug=post,
                                      status='published')
        body = post.body_v1
        tags = list(filter(None, post.tag.split('#')))
        posts = Post.object.filter(category=category,
                                   status='published')
        reklama = post.reklama
        likes = []
        for i in posts:
            if i != post and len(likes) < 3:
                 likes.append(i)
            if len(likes) == 3:
                break
        CLEANR = re.compile('<.*?>')
        og_short = re.sub(CLEANR, '', body.html)[:250]
        og_title = re.sub(CLEANR, '', post.title)
        return render(request,
                      'news/detail/detail.html',
                      {'post': post,
                       'tags': tags,
                       'body_v1': body,
                       'likes': likes,
                       'og_short': og_short,
                       'og_title': og_title,
                       'reklama': reklama})


class NewsCategory(View):
    def get(self, request, category):
        if 'query' in request.GET:
            return post_search(request)
        if category == "aktualnosci":
            posts = Post.published.all()
        else:
            posts = get_list_or_404(Post, category=category)
        count = len(posts)
        return render(request,
                    'news/category/categories.html',
                    {'posts': posts, 'category': category, 'count': count})
