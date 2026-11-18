import os
import telebot
from flask import Flask, request

# BotTokeningizni shu yerga yozing yoki Render Environment Variables'dan oling
TOKEN =9143306859:AAGTe3PZbOQR8SX3DDkkVkwvoDC4x6ElknM
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Barcha xabarlarga javob berish
@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    bot.reply_to(message, "Salom abmen qilasizmi")

# Render uchun Flask marshruti (Port yopilib qolmasligi uchun)
@app.route('/')
def index():
    return "Bot ishlayapti!", 200

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == '__main__':
    # Mahalliy test qilish uchun
    bot.remove_webhook()
    bot.infinity_polling()
