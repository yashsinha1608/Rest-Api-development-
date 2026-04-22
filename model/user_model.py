import mysql.connector
import json
class user_model():
    def __init__(self):  #constructor for connection establishment 
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="",database="flask_tutorial") #connect btw pyhon and mysql 
            self.cur=self.con.cursor(dictionary=True,buffered=True) 
            print("succesful")       
        except: 
            print("some error")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result) 
        else: 
            return "no data found"  
        
    def user_addone_model(self, data):   # ← must be indented inside class!
        try:
            self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
            self.con.commit()
            return "user added successfully"
        except Exception as e:
            return str(e)