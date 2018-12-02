from django.shortcuts import render

# Create your views here

def index(request):
    return render(request,'templates/index.html',{})
def summariser(request):
    return render(request,'templates/output.html',{})