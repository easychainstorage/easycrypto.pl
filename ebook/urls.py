from django.urls import path
from .views import EbookView, EbookDetail

app_name = 'ebook'

urlpatterns = [
    path('ebooks/<slug:ebook>/', EbookDetail.as_view(), name='ebook_detail'),
    path('ebooks', EbookView.as_view(), name='ebook'),
]
