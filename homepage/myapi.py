import requests
import json
from ast import literal_eval
from datapackage import Package

API_KEY1=''
API_KEY2=''
url1='https://api.opencagedata.com/geocode/v1/json?'
url2='https://weather.ls.hereapi.com/weather/1.0/report.json?'

def getcoordinates(city,country):
    package = Package('https://datahub.io/core/country-list/datapackage.json')
    for resource in package.resources:
      if resource.descriptor['datahub']['type'] == 'derived/csv':
          m=resource.read()
    country_code=''
    for i in m:
        if i[0]==country:
            country_code=i[1]
    if country_code=='':
        return "Please enter a valid country name"
    payload={'key':API_KEY1,'q':city,'countrycode':country_code}
    r=requests.get(url1,payload)
    data=r.json()
    return data

def getweather(coordinates):
    coordinate=literal_eval(coordinates)
    lat=coordinate['lat']
    lon=coordinate['lng']
    payload={'apiKey':API_KEY2,'latitude':lat,'longitude':lon,'oneobservation':True,'product':'observation'}
    r=requests.get(url2,params=payload,timeout=5)
    data=r.json()
    return data['observations']['location'][0]['observation'][0]

def seven(city):
    payload={'apiKey':API_KEY2,'name':city,'product':'forecast_7days'}
    r=requests.get(url2,payload)
    data=r.json()
    return data
