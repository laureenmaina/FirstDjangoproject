from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def hello(request):
    return HttpResponse("Hello there Laurine")
def evenodd(request):
    x = 25
    if x%2==0:
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is odd")

def index(request):
    return render(request,'index.html')

def variables(request):
    details = {
        "firstname":"Laurine",
        "lastname" : "eMobilis",
        "age": 60,
        "place": "Westlands",
    }
    return render(request,"variables.html",details)

def variable2(request):
    data = {
        "Empid":"101199",
        "Empname":"Laurine",
        "EmpSalary":300000,
    }
    return render(request,"variable2.html",data)

def images(request):
    return render(request,"images.html")
def images2(request):
    return render(request,"index.html")
def background(request):
    return render(request,"background.html")
