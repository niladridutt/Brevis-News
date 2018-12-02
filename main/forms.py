from django import forms

class newssite(forms.Form):
    weblink = forms.URLField(label = 'Paste url here (with https)')