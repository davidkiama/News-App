from flask import render_template
from app import app
from .request import get_news

# Views


@app.route('/')
def index():

    techcrunch = get_news('techcrunch')
    cnn = get_news('cnn')
    bbc = get_news('bbc-news')
    abc = get_news('abc-news')
    title = 'Home - News XXIV'

    return render_template('index.html', title=title, abc=abc, techcrunch=techcrunch, cnn=cnn, bbc=bbc)


@app.route('/news/<news_id>')
def news(news_id):
    return render_template('news.html', news_id=news_id)
