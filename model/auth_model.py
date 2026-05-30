import mysql.connector
from functools import wraps
import json
from flask import make_response,request
import jwt
from config.config import dbconfig
import re
class auth_model():

    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=dbconfig['hostname'], user=dbconfig['username'], password=dbconfig['password'], database=dbconfig['database'])
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True, buffered=True)
            print("successful")
        except:
            print("some error")

    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func) 
            def inner2(*args):
                endpoint=request.url_rule 
              # print(endpoint)
                authorization=request.headers.get("Authorization")
                if re.match("Bearer *([^ ]+) *$",authorization, flags=0):
                    token=authorization.split(" ")[1]
                    try:
                        jwtdecoded=jwt.decode(token,"yash",algorithms=["HS256"])
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR":"TOKEN_EXPIRED"},401)
                    role_id= jwtdecoded['payload']['role_id']
                    self.cur.execute(f"SELECT roles FROM accessibility_view WHERE endpoint='{endpoint}' ")
                    result=self.cur.fetchall()
                    if len(result)>0:
                       allowed_roles=json.loads(result[0]['roles'])    
                       if role_id in allowed_roles:
                        return func(*args)
                       else:
                        return make_response({"ERROR":"INVALID_role"},404)  
                    else:
                          return make_response({"ERROR":"UNKWON_ENDPOINT"},404)
                    
                else:
                      return make_response({"ERROR":"INVALID_TOKEN"},401)
                
            return inner2
        return inner1
     