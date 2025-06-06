from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home_page(request):
    return render(request, "blog/index.html") 
    

def posts(request):
    pass

def post_desc(request):
    pass