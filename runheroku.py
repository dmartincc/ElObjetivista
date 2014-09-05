#!flask/bin/python
from app import app
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')



