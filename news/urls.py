from django.urls import path
from .views import HomePageView, NewsDetail, NewsCategory

app_name = 'news'

urlpatterns = [
    path("", HomePageView.as_view(), name="news"),
    path('<str:category>/<slug:post>/', NewsDetail.as_view(), name='post_detail'),
    path('<str:category>', NewsCategory.as_view(), name='post_category'),
]