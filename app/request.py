

import urllib
import json
import urllib.request

from .models import News


api_key = None
base_url = None
source_url = None


def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url = app.config['NEWS_API_SOURCE_URL']


def get_news():
    '''
    Gets the json response from the request url
    '''
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['status'] == 'ok':
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def get_news_by_source(source):
    '''
    Gets the json response from the request url
    '''
    get_news_url = source_url.format(source, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['status'] == 'ok':
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Processes the movie results and transforms them to a list of objects
    '''
    news_results = []

    for news_item in news_list:

        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item['publishedAt'].split('T')[0]
        author = news_item.get('author')
        url = news_item.get('url')

        if urlToImage != 'null':
            news_object = News(title, description, urlToImage,
                               publishedAt, author, url)
            news_results.append(news_object)

    return news_results
