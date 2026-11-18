import telebot

# BotFather'dan olgan tokeningizni shu yerga yozing
TOKEN = 9143306859:AAGTe3PZbOQR8SX3DDkkVkwvoDC4x6ElknM

bot = telebot.TeleBot(TOKEN)

# Barcha turdagi matnli xabarlarni qabul qiluvchi funksiya
@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    # Foydalanuvchi nima yozishidan qat'i nazar quyidagi javobni qaytaradi
    bot.reply_to(message, "Salom abmen qilasizmi")

# Botni ishga tushirish
if __name__ == '__main__':
    print("Bot ishga tushdi...")
    bot.infinity_polling()
