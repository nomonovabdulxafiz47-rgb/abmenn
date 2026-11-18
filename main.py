import telebot

# O'zingizning tokeningiz
TOKEN = '9143306859:AAGTe3PZbOQR8SX3DDkkVkwvoDC4x6ElknM'
bot = telebot.TeleBot(TOKEN)

# Barcha xabarlarga javob qaytarish
@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    bot.reply_to(message, "Salom abmen qilasizmi")

if __name__ == '__main__':
    print("Bot ishga tushdi...")
    # Eski webhooklarni tozalab yuboradi va to'g'ridan-to'g'ri ishlaydi
    bot.remove_webhook()
    bot.infinity_polling()
