# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
import os

app = Flask(__name__)

# ✅ Carga las variables desde el entorno de Render
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/', methods=['GET'])
def home():
    return "Bot de alertas activo ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", "⚠ Señal recibida sin mensaje")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(telegram_url, json=payload)

    if response.status_code == 200:
        return "✅ Mensaje enviado", 200
    else:
        return f"❌ Error al enviar: {response.text}", 500

if __name__ == "__main__":
    # Render escucha en el puerto 10000 por defecto
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)