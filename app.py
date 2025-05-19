from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Server is running!'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').lower()
    if message == 'hi':
        reply = 'hello Jason Apacible'
    else:
        reply = "I don't understand."
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
