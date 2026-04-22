from app import app
from flask import request 
from model.user_model import user_model #importing user_model class from user_model.py file
obj=user_model()

@app.route("/user/getall") 
def user_getall_controller():
    return obj.user_getall_model() 

@app.route("/user/addone",methods=["POST"]) 
def user_addone_controller():
    #request.form   #all the data sent through postman is stored in this variable
    return obj.user_addone_model(request.form)   