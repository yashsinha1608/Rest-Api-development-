from app import app
from model.user_model import user_model #importing user_model class from user_model.py file
obj=user_model()
@app.route("/user/getall") 
def user_getall_controller():
    return obj.user_getall_model()  