from django.shortcuts import render
from newsapi import  NewsApiClient

# Create your views here.


def index(request):
    news = NewsApiClient(api_key='')
    return render(request, "index.html")
