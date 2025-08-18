from flask import jsonify
from Services.db import get_connection
class AccountRepository:
    @staticmethod
    def AllUsers():
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT DisplayName,Email,ContactInfo,Address FROM AspNetUsers")
            rows = cursor.fetchall()
            result = [{"DisplayName": row[0], "Email": row[1],"ContactInfo":row[2],"Address":row[3]} for row in rows]

            conn.close()
            return result

        except Exception as e:
            return "error"
    def Login(UserName,Password):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT DisplayName,Email,ContactInfo,Address FROM AspNetUsers WHERE UserName = ?", (UserName))
            rows = cursor.fetchall()
            result = [{"DisplayName": row[0], "Email": row[1],"ContactInfo":row[2],"Address":row[3]} for row in rows]

            conn.close()
            return result

        except Exception as e:
            return "error"
        