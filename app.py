from flask import Flask, request

app = Flask(__name__)

# تست مرورگر
@app.route("/", methods=["GET"])
def home():
    return "Bot is running!", 200


# این همون آدرسیه که روبیکا بهش پیام می‌فرسته
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("UPDATE FROM RUKA:", data)
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
