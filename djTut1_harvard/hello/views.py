from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, I am from hello.view!")
def index(request):
    return render(request,'hello/index.html')

def devid(request):
     return HttpResponse("Hello, Devid!")

def morgran(request):
     return HttpResponse("Hello, Morgran!")

# def greeting(request,name):
#      return HttpResponse(f"Hello, {name.capitalize()}")
def greeting(request,name):
     return render(request,'hello/greeting.html',{
          "name":name.capitalize()
     })