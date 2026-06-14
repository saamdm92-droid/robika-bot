from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 🔐 توکن رو اینجا بذار (یا از ENV بخون)
TOKEN = "BFGFCG0YZHLUSWZSHKDFEMFMRFQJIIKBWLKIPKEXZMJZGBMJYALMUATBMFDJGJWI"

BASE_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json

    if "update" in data:
        update = data["update"]

        if update.get("type") == "NewMessage":
            msg = update["new_message"]
            text = msg.get("text", "")
            chat_id = update.get("chat_id")

            print("User:", text)

            if text == "سلام":
                send_message(chat_id, "سلام 👋 خوش اومدی به ربات روبیکا")

            elif text == "ربات":
                send_message(chat_id, "من آنلاین هستم 🤖")

            else:
                send_message(chat_id, "دستور ناشناخته ❌")

    return "ok", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
