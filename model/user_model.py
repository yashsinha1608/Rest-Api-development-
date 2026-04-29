import mysql.connector
import json

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
            return json.dumps(result)
        else:
            return "no data found"

    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        return "user added successfully"

    def user_update_model(self, data):
        name = data['name']
        email = data['email']
        phone = data['phone']
        role = data['role']
        password = data['password']
        id = data['id']
        self.cur.execute(f"UPDATE users SET name='{name}',email='{email}',phone='{phone}',role='{role}',password='{password}' WHERE id={id}")
        if self.cur.rowcount > 0:
            return "user updated successfully"
        else:
            return "nothing to update"