from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "sk-proj-..."  # Your full OpenRouter API key
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost:3000",  # Change to your frontend URL
        "X-Title": "MyApp",  # Can be anything, just for tracking
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    try:
        res = requests.post(API_URL, headers=headers, json=data)
        res.raise_for_status()
        return res.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error: {res.status_code} - {res.text}"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "Message cannot be empty"}), 400

    reply = ask_openrouter(user_message)
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
