from django.shortcuts import render
from django.http import HttpResponse
from . models import Place,Authors
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Authors.objects.all()
    return render(request,"index.html",{'result':obj,'authors':obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request, "result.html", {'add': add,'sub':sub,'mul':mul,'div':div})
