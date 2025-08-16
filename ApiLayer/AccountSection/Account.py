from BusinessLayer.AccountSection.UserServices import AccountRepository
from flask import jsonify

class Account:
    @staticmethod
    def AllUser():
        message = AccountRepository.Login()
        return jsonify({"message": message}), 200
