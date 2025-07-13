# Flask-chatbot
Sure! Here's a **single, clean `README.md` file** that you can **copy-paste directly into your GitHub repo**:

---

```markdown
# 💬 Flask Chatbot with OpenRouter (Mistral-7B)

This is a simple chatbot project built using **Flask** as the backend (`bot.py`) and a basic **HTML frontend** (`index.html`). It uses **OpenRouter**'s AI models like `mistralai/mistral-7b-instruct` to generate intelligent responses.

---

## 🚀 Features

- ✅ Flask REST API to handle user messages
- 🤖 AI replies powered by OpenRouter (Mistral-7B)
- 🌐 Basic frontend using HTML + JavaScript
- 🔐 API key management via `.env`
- 🛡️ CORS enabled for frontend-backend communication

---

## 📁 Project Structure

```

.
├── bot.py              # Flask backend for chatbot
├── index.html          # Frontend interface
├── .env.example        # Example file to store API key (safe to share)
├── requirements.txt    # Python dependencies
└── README.md           # Project info and usage guide

````

---

## 🧪 Installation and Setup

### 1. Clone this repository

```bash
git clone https://github.com/dolithachowdary/Flask-chatbot.git
cd Flask-chatbot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenRouter API key

Create a `.env` file in the root folder:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Do **not** upload this file to GitHub.

---

## ▶️ Running the App

### 1. Start the Flask server

```bash
python bot.py
```

Server runs at: `http://localhost:5000`

### 2. Open the Chatbot UI

Just open `index.html` in any browser and start chatting!

---

## 📡 API Endpoint

**POST** `/chat`

**Request body:**

```json
{
  "message": "Hello!"
}
```

**Response:**

```json
{
  "response": "Hi there! How can I help you today?"
}
```

---

## 🔒 Security Tips

* Store your real API key only in a local `.env` file.
* Never commit `.env` to GitHub.
* Share `.env.example` instead, like this:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## 📄 License

This project is open-source and licensed under the MIT License.

---

## 🙋‍♀️ Author

Made with ❤️ by [dolithachowdary](https://github.com/dolithachowdary)

---

## ⭐️ Support

If you found this useful, please give the repo a ⭐ on GitHub!

```


