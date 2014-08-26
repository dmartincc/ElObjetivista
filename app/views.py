from flask import render_template
from flask import jsonify
from app import app
import getNews 
import json
import time, random
import re
from nltk.corpus import stopwords

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
    input = getNews.fetchNews()  
    jsonData = json.loads(input) 
    news  = jsonData['value']['items'] 
    now = time.strftime("%c")
    range=len(news)-30
    data=random.sample(news, 100)
    a = ['a','b','c','d']
    for item in data:
        item["div"]=a[random.randint(0,3)]
    return render_template("index2.html",
                            #title = 'Home',
                            news = data[0:19],
                            news2 = data[20:39])

@app.route('/noticias')
def news(): 
    
    return render_template("noticias.html",
                            title="noticias")
