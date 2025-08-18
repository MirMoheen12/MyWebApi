from BusinessLayer.AccountSection.UserServices import AccountRepository
from flask import jsonify

class Account:
    @staticmethod
    def AllUser():
        message = AccountRepository.AllUsers()
        return jsonify({"message": message}), 200
    @staticmethod
    def Login(UserName, Password):
        message = AccountRepository.Login(UserName, Password)
        return jsonify({"message": message}), 200