from app import app
from flask import request,send_file
from model.user_model import user_model #importing user_model class from user_model.py file
obj=user_model()
from datetime import datetime 
 

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

@app.route("/user/getall/limit/<limit>/page/<page>",methods=["GET"]) 
def user_pgination_controller(limit,page):
   
    return obj.user_pagination_model(limit,page)


@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def user_upload_avatar_controller(uid):
    file=request.files['avatar'] #request.files['avatar'] = one specific item from the bag request.files = the whole bag
    uniquefilename=str(datetime.now().timestamp()).replace(".", "")
    filenamesplit=file.filename.split(".")
    ext=filenamesplit[len(filenamesplit)-1] 
    finalfilepath=f"uploads/{uniquefilename}.{ext}"
    file.save(finalfilepath)
    return obj.user_upload_avatar_model(uid,finalfilepath)

#yeh thoda deakhna hai utna nahi aaya samajh theory part
@app.route("/uploads/<filename>")
def user_getavatar_controller(filename):
     
     return send_file(f"uploads/{filename }")    


@app.route("/user/login",methods=["POST"])
def user_login_controller():
    request.form
    return obj.user_login_model(request.form)