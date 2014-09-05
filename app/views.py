from flask import render_template, jsonify
from app import app
import getNews , json, time, random, re

@app.route('/')
def index(): 
    input = getNews.fetchNews()
    jsonData = json.loads(input) 
    news  = jsonData['value']['items'] 
    now = time.strftime("%c")
    range=len(news)-30
    data=random.sample(news, range)
    return render_template("index.html",
                            #title = 'Home',
                            news = data,
                            entities = data,
                            now= now)

@app.route('/test')
def index2(): 
    input = getNews.fetchApi('http://www.elobjetivista.com/api/0.1/articles')  
    jsonData = json.loads(input) 
    news  = jsonData['result']

    """input = getNews.fetchNews()
    jsonData = json.loads(input) 
    news  = jsonData['value']['items'] 
    now = time.strftime("%c")
    range=len(news)-30
    data=random.sample(news, range)"""
    
    a = ['a','b','c','d']
    for item in news:
        item["div"]=a[random.randint(0,3)]
    return render_template("index2.html",
                            #title = 'Home',
                            news = data)

@app.route('/noticias')
def news():     
    return render_template("noticias.html",
                            title="noticias")
