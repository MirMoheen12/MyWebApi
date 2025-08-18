import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from flask import Flask, jsonify, request
from AccountSection.Account import Account
app = Flask(__name__)

@app.route('/api/Account/AllUsers', methods=['GET'])
def test_api():
    res=Account.AllUser()
    return res
@app.route('/api/Account/Login', methods=['POST'])
def Login():
    data=request.get_json()
    UserName = data.get('UserName')
    Password = data.get('Password')
    Msg="UserName: {}, Password: {}".format(UserName, Password)
    #res=Account.Login(UserName, Password)
    return jsonify({"message": Msg})
  

if __name__ == "__main__":
    app.run(debug=True, port=5000)

