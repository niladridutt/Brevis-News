from django.shortcuts import render
from .Newsletterapi import *
from .forms import newssite
from django.shortcuts import redirect
# Create your views here

def index(request):
    trends = trending()
    if request.method == 'POST':
        form = newssite(request.POST)
        if form.is_valid():
            request.session['weblink'] = form.cleaned_data['weblink']
            return redirect('summariser')
    form = newssite()
    return render(request,'main/index.html',{'trending_terms':trends[0],'trending_urls':trends[1],'form': form})
def summariser(request):
    newsurl = request.session.get('weblink')
    text = get_text(newsurl)
    return render(request,'main/output.html',{'text':text})