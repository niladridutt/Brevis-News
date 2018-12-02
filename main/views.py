from django.shortcuts import render

# Create your views here

def index(request):
    return render(request,'templates/index.html',{})
def output(request):
    return render(request,'templates/output.html',{})