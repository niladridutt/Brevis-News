from django import forms

class WebsiteForm(forms.Form):
    weblink = forms.URLField(label = 'Paste url here (with https)')