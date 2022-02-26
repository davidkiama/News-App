from flask import render_template
from app import app

# Views


@app.route('/')
def index():
    title = 'Home - News XXIV'
    return render_template('index.html', title=title)


@app.route('/news/<news_id>')
def news(news_id):
    return render_template('news.html', news_id=news_id)
