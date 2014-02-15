from flask import render_template
from flask import jsonify
from app import app
import getNews 
import json
import time, random


 

@app.route('/')
def index(): 
    input = getNews.getData()
    jsonData = json.loads(input) 
    news  = jsonData['value']['items'] 
    now = time.strftime("%c")
    range=len(news)-30
    data=random.sample(news, 100)
    print data
    return render_template("index.html",
                            #title = 'Home',
                            news = data[-10:],
                            entities = news,
                            now= now)

@app.route('/analytics')
def analytics(): 
    input = getNews.getData()
    jsonData = json.loads(input) 
    news  = jsonData['value']['items']
    words=[]
    for art in news:
        if getNews.whatisthis(art['title']) == "unicode string":
            words_title=art['title'].encode('utf-8','ignore').split() 
        else: 
            words_title=str(art['title']).split()        
        words.extend(words_title)

    wordFreqD = {}   
    sum = 0
    for i in range(len(words)):
        for char in '@%#?.!/;:<",':  
            words[i] = words[i].replace(char,'')
        wordFreqD[words[i]] = wordFreqD.get(words[i], 0)+1

    output = [{k:v} for v,k in sorted([(v,k) for k,v in wordFreqD.items()],reverse=True)]

    return str(output)    

   
    

