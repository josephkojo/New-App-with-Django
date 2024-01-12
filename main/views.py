from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.


# importing api
from django.shortcuts import render
from newsapi import NewsApiClient


# # Create your views here.
# def index(request):
#     newsapi = NewsApiClient(api_key='YOURAPIKEY')
#     top = newsapi.get_top_headlines(sources='techcrunch')
#
#     l = top['articles']
#     desc = []
#     news = []
#     img = []
#
#     for i in range(len(l)):
#         f = l[i]
#         news.append(f['title'])
#         desc.append(f['description'])
#         img.append(f['urlToImage'])
#     mylist = zip(news, desc, img)

# return render(request, 'index.html', context={"mylist": mylist})


def index(request):
    news = NewsApiClient(api_key='7c34248301904fc58f139bc0014cd84a')
    top_headlines = news.get_top_headlines(sources="techcrunch")
    articles = top_headlines['articles']
    description = []
    news_title = []
    images = []
    for i in range(len(articles)):
        individual_news = articles[i]
        news_title.append(individual_news["title"])
        description.append(individual_news['description'])
        images.append(individual_news['urlToImage'])
    news_information = zip(news_title, description, images)
    news_dict = {"news_dict": news_information}
    return render(request, "index.html", news_dict)
