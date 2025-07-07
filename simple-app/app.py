from flask import Flask, request, jsonify

app = Flask(__name__)

#Initialize the counter
post_request_count = 0

@app.route('/post', methods=['POST'])
def post_request():
    global post_request_count
    post_request_count += 1
    return jsonify({"massage":"POST request recived"}), 200

@app.route('/get', methods=['GET'])
def get_request():
    return jsonify({"post_request_count": post_request_count}), 200

if __name__ == '__main__':
    app.run(port=1888, debug=True)
