from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from distributed.http.utils import redirect
# Create your views here.

def check(request):
    if 'image' in request.FILES:
        image = request.FILES['image']
        
        
def start_form(request):
    return render(request,"User/start.html")

def start(request):
    return render(request,'User/check.html')