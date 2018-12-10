from django.shortcuts import render, redirect
from .Newsletterapi import *
from .forms import WebsiteForm
from django.shortcuts import redirect
# Create your views here

def index(request):
    trends = trending()
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            request.session['weblink'] = form.cleaned_data['weblink']
            return redirect('summariser')
    form = WebsiteForm()
    return render(request,'main/index.html',{'trending_terms':trends[0],'trending_urls':trends[1],'form': form})

    
def summariser(request):
    newsurl = request.session.get('weblink')
    text = get_text(newsurl)
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            request.session['weblink'] = form.cleaned_data['weblink']
            return redirect('summariser')
    form = WebsiteForm()
    return render(request,'main/output.html',{'text':text,'form': form})
