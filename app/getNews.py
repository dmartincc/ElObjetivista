import urllib, httplib
import json
import time

def fetchsamples():
    url = "http://pipes.yahoo.com/pipes/pipe.run?_id=9c8c3a4b218215e6e02182787a522372&_render=json"
    response = urllib.urlopen(url)
    data = response.read()
    return data

def getData():       
    input = fetchsamples()
    #file = open('app/jsonOutput.json','w')
    #file.write(input)
    #file.close()
    #jsonData = json.loads(input)
    #rawData  = jsonData['value']['items']
    return input



