from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # @ denotes a 
def welcome():
    return render_template("welcome.html")

