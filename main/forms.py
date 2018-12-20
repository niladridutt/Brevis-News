from django import forms
""" Class based form model to extend usage to add ability to save summaries into database"""
class WebsiteForm(forms.Form):
    weblink = forms.URLField(label = 'Paste url here (with https)')
