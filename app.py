from flask import Flask 
app = Flask(__name__)

@app.route("/") #decoraors ie app.route naam ka eak function hai aur uske andar joh abhi hum likhe hai voh sab paas hoga
def welcome():
    return "hello" 

@app.route("/home") 
def home():
    return "this is home page" 
@app.route("/chill") 
def chill():
    return "this is just a  page" 

import user_controller