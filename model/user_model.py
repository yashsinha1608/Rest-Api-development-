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
        name = data['name']
        email = data['email']
        phone = data['phone']
        role = data['role']
        password = data['password']
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{name}','{email}','{phone}','{role}','{password}')")
        return "user added successfully"

    def user_update_model(self, data):   # ← must be indented inside class!
            self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']} ")
         #   self.con.commit()
            if self.cur.rowcount>0: #if rowcount=0 ie same data is given 
                return "user updated successfully"
            else:
                return "nothing to update"

    def user_delete_model(self, id):   # ← must be indented inside class!
            self.cur.execute(f"DELETE FROM users WHERE id={id}")
         #   self.con.commit()
            if self.cur.rowcount>0: #if rowcount=0 ie same data is given 
                return "user deleted successfully"
            else:
                return "nothing to delete" 