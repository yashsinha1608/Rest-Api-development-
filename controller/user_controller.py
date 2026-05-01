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

@app.route("/user/update",methods=["PUT"]) 
def user_update_controller():
   # print(request.form)  # ← add this line
    return obj.user_update_model(request.form)


@app.route("/user/delete/<id>",methods=["DELETE"]) 
def user_delete_controller(id):
   
    return obj.user_delete_model(id)


@app.route("/user/patch/<id>",methods=["PATCH"]) 
def user_patch_controller(id):
   
    return obj.user_patch_model(request.form,id)