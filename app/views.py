from flask import render_template
from flask import jsonify
from app import app
from getNews import getData
import json

@app.route('/')
def index():
    input = getData()
    #input = open('app/jsonOutput.json','r')
    #jsonData = json.loads(input.read())
    #input.close()
    jsonData = json.loads(input)    
    news  = jsonData['value']['items']
    return render_template("index.html",
                            #title = 'Home',
                            news = news)


    

