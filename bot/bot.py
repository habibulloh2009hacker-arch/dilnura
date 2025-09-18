import telebot

# Bot tokeningizni shu joyga yozing
bot = telebot.TeleBot("8440946740:AAFGL00tA4s8F1Ai1cmcyTTKbZU437NpQHk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    messages = [
        "1) Assalomu alaykum Dilnura, yaxshimisiz 😊",
        "2) Shuni bilingki, siz judayam ajoyibsiz 🤭",
        "3) Asabizi doimo yaxshi qiling hop 😁",
        "4) Siz men ko‘rgan eng zo‘r qizsiz 🎀",
        "5) Yana qo‘shimcha yaxshi so‘zlar 💐😊"
    ]

    for msg in messages:
        bot.send_message(chat_id, msg)

# Botni doimiy ishlatish uchun
bot.polling(none_stop=True)
