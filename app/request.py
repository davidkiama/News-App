from app import app

import urllib
import json

from .models import news


News = news.News


# Getting the api_key from the config file
api_key = app.config['NEWS_API_KEY']

# Getting the base_url from the config file
base_url = app.config['NEWS_API_BASE_URL']


def get_news(source):
    '''
    Gets the json response from the request url
    '''

    get_news_url = base_url.format(source, api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Processes the movie results and transforms them to a list of objects
    '''

    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        author = news_item.get('author')
        url = news_item.get('url')

        if urlToImage:
            news_object = News(id, title, description, urlToImage, author, url)
            news_results.append(news_object)

    return news_results
