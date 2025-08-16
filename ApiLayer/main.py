import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, jsonify
from AccountSection.Account import Account
app = Flask(__name__)

@app.route('/api/Home/TestApi2', methods=['GET'])
def test_api():
    res=Account.AllUser()
    return res
if __name__ == "__main__":
    app.run()
