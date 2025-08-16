from flask import jsonify
from Services.db import get_connection
class AccountRepository:
    @staticmethod
    def Login():
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT TOP 5 Id, UserName FROM AspNetUsers")
            rows = cursor.fetchall()
            result = [{"Id": row[0], "Name": row[1]} for row in rows]

            conn.close()
            return result

        except Exception as e:
            return "error"

        