from flask import render_template
from flask import jsonify
from app import app
import getNews 
import json
import time, random
import re
from nltk.corpus import stopwords

input = getNews.getData()
jsonData = json.loads(input) 
news  = jsonData['value']['items'] 
 

@app.route('/')
def index():     
    now = time.strftime("%c")
    range=len(news)-30
    data=random.sample(news, 100)
    return render_template("index.html",
                            #title = 'Home',
                            news = data[-10:],
                            entities = data,
                            now= now)

@app.route('/analytics')
def analytics(): 
    now = time.strftime("%c")
    words=[]
    for art in news:
        if getNews.whatisthis(art['title']) == "unicode string":
            words_title=art['title'].encode('utf-8','ignore').replace("@%#()&?.!/;':\"<,",'').split()
        else: 
            words_title=str(art['title']).split()       
        words.extend(words_title)
    
    #This is the simple way to remove stop words
    important_words=[]
    for word in words:
        if word.lower() not in stopwords.words('spanish'):
            important_words.append(word)
        
    wordFreqD = {}   
    sum = 0
    for i in range(len(important_words)):
        for char in '\"':  
            important_words[i] = important_words[i].replace(char,'')
        wordFreqD[important_words[i]] = wordFreqD.get(important_words[i], 0)+1

    output = [{"children":{"packageName":"entities","className":k,"value":v}} for v,k in sorted([(v,k) for k,v in wordFreqD.items()],reverse=True)]
    output2=output[:20]
    return render_template("analytics.html",                            
                            entities = output2,
                            now= now)

       

   
    

