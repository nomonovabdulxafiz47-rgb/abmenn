import os
import telebot
from flask import Flask, request

# Tokeningizni to'g'ridan-to'g'ri yozamiz
TOKEN = '9143306859:AAGTe3PZbOQR8SX3DDkkVkwvoDC4x6ElknM'
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Barcha xabarlarga javob beruvchi funksiya
@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    bot.reply_to(message, "Salom abmen qilasizmi")

# Render uchun asosiy sahifa
@app.route('/')
def index():
    return "Bot ishlayapti!", 200

# Telegramdan keladigan xabarlarni qabul qilish uchun webhook manzil
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200
    else:
        return "Forbidden", 403

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
