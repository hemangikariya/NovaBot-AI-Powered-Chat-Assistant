from flask import Flask, request, jsonify
from chatbot_logic import get_bot_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "✅ NovaBot Backend is Live!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    context = data.get('context', '') 
    response = get_bot_response(message, context)

    if isinstance(response, dict):
        return jsonify({
            "response": response["text"],
            "options": response.get("options", []),
            "topic": response.get("topic", "")
        })

    return jsonify({ "response": "Something went wrong!" })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(debug=False, host="0.0.0.0", port=port)
