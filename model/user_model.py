import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="", database="flask_tutorial")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True, buffered=True)
            print("successful")
        except:
            print("some error")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:
            res =make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return make_response({"message":"no data found"},204) # 204 is a http code which does not need a body  

    def user_addone_model(self, data):
        name = data['name']
        email = data['email']
        phone = data['phone']
        role = data['role']
        password = data['password']
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{name}','{email}','{phone}','{role}','{password}')")
        return make_response({"message":"user added"},201)

    def user_update_model(self, data):   # ← must be indented inside class!
            self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']} ")
         #   self.con.commit()
            if self.cur.rowcount>0: #if rowcount=0 ie same data is given 
                return make_response({"message":"user updated successfully"},201)
            else:
                return make_response({"message":"nothing to update"},202)

    def user_delete_model(self, id):   # ← must be indented inside class!
            self.cur.execute(f"DELETE FROM users WHERE id={id}")
         #   self.con.commit()
            if self.cur.rowcount>0: #if rowcount=0 ie same data is given 
                return make_response({"message":"user deleted successfully"},200)
            else:
                return make_response({"message":"nothing to delete"},204)