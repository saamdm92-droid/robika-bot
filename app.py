from flask import Flask, request
import requests

app = Flask(__name__)

# توکن ربات
TOKEN = "BFGFCG0YZHLUSWZSHKDFEMFMRFQJIIKBWLKIPKEXZMJZGBMJYALMUATBMFDJGJWI"

API = "https://botapi.rubika.ir/v3/"

def send(chat_id, text):
    try:
        requests.post(
            API + "sendMessage",
            json={
                "auth": TOKEN,
                "chat_id": chat_id,
                "text": text
            }
        )
    except Exception as e:
        print("Send Error:", e)

# صفحه اصلی برای تست
@app.route("/")
def home():
    return "Bot is running!"

# وبهوک
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    print("DATA:", data)

    text = data.get("text", "")
    chat_id = data.get("chat_id")

    if chat_id:
        if text == "/start":
            send(chat_id, "سلام 👋 ربات روشن است")

        elif text.startswith("/create"):
            country = text.replace("/create", "").strip()
            if country:
                send(chat_id, f"کشور {country} ساخته شد ✔️")
            else:
                send(chat_id, "مثال: /create Iran")

        elif text == "/list":
            send(chat_id, "فعلاً لیست کشورها خالی است")

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
