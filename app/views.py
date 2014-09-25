# -*- coding: utf-8 -*
from flask import render_template, jsonify, request
from app import app
import getNews , json, time, random, re


@app.route("/")
def landing():
    title='El periódico de las tendencias sociales y basado en datos'
    return render_template("landing.html",
                            title = title)

@app.route('/works')
def works(): 
    input = getNews.fetchNews()
    jsonData = json.loads(input) 
    news  = jsonData['value']['items'] 
    now = time.strftime("%c")
    range=len(news)-50
    news=random.sample(news, range)
    a = ['a','b','c','d']    
    data =[]
    for item in news:
        item["div"]=a[random.randint(0,3)]
        data.append(item)

    print data[0].keys()

    input = getNews.fetchApi('http://elobjetivista-api.herokuapp.com/trends')  
    jsonData = json.loads(input) 
    trends  = jsonData['items'][0]

    return render_template("index3.html",
                            title = 'Portada',
                            trends = trends,
                            news = data)


@app.route('/portada')
def index(): 
    input = getNews.fetchApi('http://elobjetivista-api.herokuapp.com/articles')  
    jsonData = json.loads(input) 
    news  = jsonData['items']
    a = ['a','b','c','d']
    b = ['w1','w2','w3']
    data =[]
    for item in news:
        item["div"]=a[random.randint(0,3)]
        item["w"]=b[random.randint(0,2)]
        data.append(item)
    

    input = getNews.fetchApi('http://elobjetivista-api.herokuapp.com/trends')  
    jsonData = json.loads(input) 
    trends  = jsonData['items'][0]
    
    return render_template("index2.html",
                            #title = 'Home',
                            trends = trends,
                            news = data)

@app.route('/<category>')
def category(category): 
    input = getNews.fetchApi('http://elobjetivista-api.herokuapp.com/articles/'+category.encode('utf-8'))  
    jsonData = json.loads(input) 
    news  = jsonData['items']
    a = ['a','b','c','d']
    b = ['w1','w2','w3']
    data =[]
    for item in news:
        item["div"]=a[random.randint(0,3)]
        item["w"]=b[random.randint(0,2)]
        data.append(item)
    

    input = getNews.fetchApi('http://elobjetivista-api.herokuapp.com/trends')  
    jsonData = json.loads(input) 
    trends  = jsonData['items'][0]
    
    return render_template("index2.html",
                            title = category,
                            trends = trends,
                            news = data)

@app.route('/articles/id/<idnum>')
def news(idnum):     
    input = getNews.fetchApi('http://elobjetivista-api.herokuapp.com/articles/id/'+idnum)  
    jsonData = json.loads(input)
    print jsonData 
    news  = jsonData['items'][0]

    return render_template("noticias.html",
                            title="noticias",
                            data=news)


@app.route('/sitemap.xml')
def sitemap():
    url_root = request.url_root[:-1]
    rules = app.url_map.iter_rules()
    return render_template('sitemap.xml', url_root=url_root, rules=rules)