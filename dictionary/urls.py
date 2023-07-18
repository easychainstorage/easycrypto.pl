from django.urls import path
from .views import GlossaryPage

app_name = 'dictionary'


urlpatterns = [
     # Widoki posta.
     path('slownik', GlossaryPage.as_view(), name='dictionary'),
]
