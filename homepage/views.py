from django.shortcuts import render
from . import myapi

def homepage(request):
    return render(request,'homepage.html',context=None)

def search(request):
    city=request.POST.get('city')
    country=request.POST.get('country')
    data=myapi.getcoordinates(city,country)
    return render(request,'result.html',{'data':data})

def getweather(request):
    coordinates=request.POST.get('coordinates')
    data=myapi.getweather(coordinates)
    return render(request,'weather.html',{'data':data})