from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#To display from a html file
def demo(request):
    name="India"
    #passing value to a html file
    return render(request,"home.html",{'obj':name})

def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res1=x+y
    res2=x-y
    res3=x*y
    res4=x/y
    return render(request,"result.html",{'add':res1,'sub':res2,'mul':res3,'div':res4})

def contact(request):
    return HttpResponse("Iam contact")