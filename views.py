from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):

    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=81a0b2956c214ccc9f802808ce106de5")
    news_api_request_india=requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=81a0b2956c214ccc9f802808ce106de5")
    news_cat=requests.get("https://newsapi.org/v2/top-headlines?category=entertainment&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
    headline=requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=81a0b2956c214ccc9f802808ce106de5")
    news_api_request_entertainment=requests.get("https://newsapi.org/v2/top-headlines?category=entertainment&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
    news_api_request_sports=requests.get("https://newsapi.org/v2/top-headlines?category=sports&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
    news_api_request_health=requests.get("https://newsapi.org/v2/top-headlines?category=health&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")


    data=True
    covid=None
    covid_api=None
    while(data):
        try:
         covid=requests.get("https://api.covid19api.com/summary")
         covid_api=covid.json()['Countries']
         data=False
        except:
         data=True


    api=json.loads(news_api_request.content)
    api_india=json.loads(news_api_request_india.content)
    api_cat=json.loads(news_cat.content)
    api_head=json.loads(headline.content)
    sports=json.loads(news_api_request_sports.content)
    entertainment=json.loads(news_api_request_entertainment.content)
    health=json.loads(news_api_request_health.content)
    

    param={
        'api':api,
        'api_india':api_india,
        'api_cat':api_cat,
        'covid_api':covid_api,
        'entertainment':entertainment,
        'sports':sports,
        'health':health,
        'api_head':api_head
       
    }
    return render(request,'news/index.html',param)


def categories(request):
        news_api_request_india=requests.get("https://newsapi.org/v2/top-headlines?category=entertainment&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        news_api_request_sports=requests.get("https://newsapi.org/v2/top-headlines?category=sports&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        news_api_request_health=requests.get("https://newsapi.org/v2/top-headlines?category=health&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        news_api_request_bussiness=requests.get("https://newsapi.org/v2/top-headlines?category=business&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        news_api_request_technology=requests.get("https://newsapi.org/v2/top-headlines?category=technology&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        news_api_request_science=requests.get("https://newsapi.org/v2/top-headlines?category=science&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        news_api_request_general=requests.get("https://newsapi.org/v2/top-headlines?category=general&language=en&country=in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        news_api_request_head=requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=81a0b2956c214ccc9f802808ce106de5")
        
        sports=json.loads(news_api_request_sports.content)
        health=json.loads(news_api_request_health.content)
        bussiness=json.loads(news_api_request_bussiness.content)
        technology=json.loads(news_api_request_technology.content)
        science=json.loads(news_api_request_science.content)
        general=json.loads(news_api_request_general.content)
        head=json.loads(news_api_request_head.content)
      
        api_india=json.loads(news_api_request_india.content)
        param={
        
        'api_india':api_india,
        'sports':sports,
        'health':health,
        'bussiness':bussiness,
        'technology':technology,
        'science':science,
        'general':general,
        'head':head
        }

        return render(request,'news/categories.html',param)
