from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/Home/TestApi2', methods=['GET'])
def test_api():
    Message = "Login API is not implemented yet."
    return jsonify({"message": Message}), 501

if __name__ == "__main__":
    app.run()
