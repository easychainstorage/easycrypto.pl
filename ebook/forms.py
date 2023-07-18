from django import forms


class EbookDownloadForm(forms.Form):
    email = forms.EmailField(label='Twój e-mail')