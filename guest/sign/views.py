from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
'''
def index(request):
    return HttpResponse("Hello Django!")
'''

def index(request):
    return render (request,"index.html")

def add(request,a,b):
    s = int(a)+int(b)
    return HttpResponse(str(s))
