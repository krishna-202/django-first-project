from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def result(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    add=num1+num2
    return render(request,"result.html",{'result':add})
