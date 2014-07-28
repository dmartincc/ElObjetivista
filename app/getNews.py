import urllib, httplib
import json
import time

def fetchNews():
    url = "http://pipes.yahoo.com/pipes/pipe.run?_id=9c8c3a4b218215e6e02182787a522372&_render=json"
    response = urllib.urlopen(url)
    data = response.read()
    return data




