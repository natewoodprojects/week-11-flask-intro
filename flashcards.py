from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/") # @ denotes a 
def welcome():
    return "Welcome to my Flash Cards application!"


@app.route("/date") # @ denotes a 
def date():
    return "This page was served at " + str(datetime.now())

counter = 0

@app.route("/count_views") # @ denotes a 
def count_views():
    global counter
    counter += 1
    return "This page was served " + str(counter) + " times"