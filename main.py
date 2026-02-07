import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    try:
        res = requests.post(API_URL, headers=headers, json=data)
        res.raise_for_status()
        return res.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        status_code = res.status_code if 'res' in locals() else "N/A"
        error_text = res.text if 'res' in locals() else str(e)
        return f"Error: {status_code} - {error_text}"

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "Message cannot be empty"}), 400

    reply = ask_groq(user_message)
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
