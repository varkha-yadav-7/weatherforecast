from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('search/',views.search),
    path('search/getweather/',views.getweather),
]