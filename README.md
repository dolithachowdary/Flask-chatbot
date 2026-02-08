# 💬 Modern Flask Chatbot (Groq AI)

A premium, interactive chatbot application built with **Flask**, **Vanilla JS**, and **Groq AI**. Featuring a modern sidebar UI, real-time typing animations, and rich Markdown formatting.

---

## 🚀 Key Features

- 🧠 **AI-Powered**: Intellectual responses powered by Groq's `llama-3.3-70b-versatile` model.
- ✨ **Typing Animation**: ChatGPT-like character-by-character typing effect for a natural feel.
- 💬 **Rich Markdown Support**: Full support for bold, italics, code blocks (with syntax highlighting), lists, and tables.
- ⏳ **Thinking Indicator**: Sequential pulsing dots animation while waiting for AI processing.
- � **Premium UI**: 
    - Responsive Glassmorphic Sidebar.
    - Personalised Avatars (via Dicebear).
    - Dark-themed code blocks.
    - Interactive Emoji Picker.
    - Smooth slide-in message animations.

---

## 📁 Project Structure

```
.
├── main.py             # Flask backend & API integration
├── index.html          # Modern SPA frontend (HTML/CSS/JS)
├── .env                # Private API configuration
├── requirements.txt    # Backend dependencies
└── README.md           # Project documentation
```

---

## 🧪 Installation and Setup

### 1. Clone this repository

```bash
git clone https://github.com/dolithachowdary/Flask-chatbot.git
cd Flask-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the App

### 1. Start the Flask server

```bash
python main.py
```

Server will start at: `http://localhost:5000`

### 2. Open the Chatbot

Simply navigate to `http://localhost:5000` in your web browser.

---

## 📡 API Reference

### Send Message
- **Endpoint**: `/chat`
- **Method**: `POST`
- **Payload**:
  ```json
  { "message": "Why is the sky blue?" }
  ```
- **Response**:
  ```json
  { "response": "The sky appears blue because of Rayleigh scattering..." }
  ```

---

## 🔒 Security

- API keys are managed securely via environment variables.
- `.env` is ignored by git to prevent accidental exposure.
- CORS is configured for secure communication.

---

## 🙋‍♀️ Author

Made with ❤️ by [dolithachowdary](https://github.com/dolithachowdary)

---

## ⭐️ Support

If you found this useful, please give the repo a ⭐ on GitHub!
