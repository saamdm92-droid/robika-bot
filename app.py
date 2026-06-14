from flask import Flask, request
import requests

app = Flask(__name__)

# 🔴 توکن ربات تو
TOKEN = TOKEN = "BFGFCG0YZHLUSWZSHKDFEMFMRFQJIIKBWLKIPKEXZMJZGBMJYALMUATBMFDJGJWI"

API = "https://botapi.rubika.ir/v3/"

def send(chat_id, text):
    try:
        requests.post(API + "sendMessage", json={
            "auth": TOKEN,
            "chat_id": chat_id,
            "text": text
        })
    except:
        pass


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    text = data.get("text", "")
    chat_id = data.get("chat_id")

    if not chat_id:
        return "no chat"

    # دستورات ساده تست
    if text == "/start":
        send(chat_id, "سلام 👋 ربات روشن است ✔️")

    elif text.startswith("/create"):
        name = text.replace("/create", "").strip()
        if name:
            send(chat_id, f"کشور {name} ساخته شد ✔️")
        else:
            send(chat_id, "اسم کشور رو بنویس ❌ مثال: /create Iran")

    elif text.startswith("/list"):
        send(chat_id, "📋 هنوز لیست ساده است (در نسخه بعدی کامل میشه)")

    else:
        send(chat_id, "❓ دستور ناشناخته")

    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
