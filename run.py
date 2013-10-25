#!flask/bin/python
from app import app
from getNews import getData
import datetime, threading
import time

app.run(debug = True)


