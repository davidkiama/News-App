from flask import render_template, url_for
from app import app
from .request import get_news, get_news_by_source

# Views


@app.route('/')
def index():
    news_list = get_news()
    title = 'Home - News XXIV'
    return render_template('index.html', title=title, news_list=news_list)


@app.route('/news/<source>')
def news(source):
    news_list = get_news_by_source(source)
    news_page = source.capitalize()
    title = f'{news_page} - News XXIV'
    return render_template('news.html', title=title, news_list=news_list, )
