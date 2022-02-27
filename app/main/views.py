from flask import render_template, url_for
from . import main
from ..request import get_news, get_news_by_source
from ..models import News

# Views


@main.route('/')
def index():
    news_list = get_news()
    title = 'Home - News XXIV'
    return render_template('index.html', title=title, news_list=news_list)


@main.route('/news/<source>')
def news(source):
    news_list = get_news_by_source(source)
    news_page = source.upper()
    title = f'{news_page} - News XXIV'
    return render_template('news.html', title=title, news_list=news_list, news_page=news_page)
