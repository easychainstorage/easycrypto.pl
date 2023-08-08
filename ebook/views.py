from django.views import View
from .models import Ebook, EbookEmails
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .forms import EbookDownloadForm
from news.views import post_search
from sendgrid.helpers.mail import Mail, HtmlContent, PlainTextContent, Content
from sendgrid import SendGridAPIClient
from bs4 import BeautifulSoup
from django.conf import settings


def read_file(path):
    with open(path) as fp:
        return fp.read()

class EbookView(View):
    def get(self, request):
        if 'query' in request.GET:
            return post_search(request)
        ebooks = get_list_or_404(Ebook)
        return render(request,
                      'ebook/listing.html',
                      {'ebooks': ebooks})


class EbookDetail(View):
    def get(self, request, ebook):
        if 'query' in request.GET:
            return post_search(request)
        count_download = EbookEmails.objects.count()
        ebook = get_object_or_404(Ebook, slug=ebook)
        form = EbookDownloadForm()
        return render(request,
                      'ebook/detail.html',
                      {'ebook': ebook, 'form': form, 'count_download': count_download})

    def post(self, request, ebook):
        ebook = get_object_or_404(Ebook, slug=ebook)
        soup = read_file('templates/ebook/email.html')
        soup = soup.replace('<a href="#" id="pobierz"', f'<a href="{ebook.get_presigned_url()}" id="pobierz"')

        html_text = str(soup)
        html_content = HtmlContent(html_text)
        soup = BeautifulSoup(html_text, features='lxml')

        plain_text = soup.get_text()
        plain_text_content = Content("text/plain", plain_text)

        form = EbookDownloadForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = Mail(
                from_email=('kontakt@easycrypto.pl', "Easycrypto.pl"),
                to_emails=email,
                subject='Twój ebook od easycrypto.pl',
                plain_text_content=plain_text_content,
                html_content=html_content)
            EbookEmails.objects.create(
                email=email,
                title=ebook.title
            )
            try:
                sg = SendGridAPIClient(settings.SENDGRIP_API_KEY)
                response = sg.send(message)
            except Exception as e:
                print(e)
            return render(request, 'ebook/success.html', {'ebook': ebook})
        return render(request, 'ebook/detail.html', {'ebook': ebook, 'form': form})
