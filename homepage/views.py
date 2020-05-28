from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import myapi

error=''

def homepage(request):
    return render(request,'homepage.html',{'error':error})

def search(request):
    global error
    error=''
    city=request.POST.get('city')
    country=request.POST.get('country')
    data=myapi.getcoordinates(city,country)
    if data=='Please enter a valid country name':
        error=data
        return HttpResponseRedirect('/homepage/')
        '''elif data['status_code']==200:
        return render(request,'result.html',{'data':data,'city':city})'''
    else:
        error='No such city found'
        return render(request,'result.html',{'data':data,'city':city})
        #return HttpResponseRedirect('/homepage/')

def getweather(request):
    coordinates=request.POST.get('coordinates')
    data=myapi.getweather(coordinates)
    city=data['city']
    seven=myapi.seven(city)
    return render(request,'weather.html',{'data':data,'seven':seven})