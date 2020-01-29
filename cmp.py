import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ["start"])
def wlcm(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item = types.KeyboardButton("Random cat sticker")

    markup.add(item)

    bot.send_message(message.chat.id, "Приветик, {0.first_name}!\nУ меня один ссаный вопрос, ты шо, ебанутый, чтобы сюда заходить?".format(message.from_user, bot.get_me()), parse_mode = "html", reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def randcatsticker(message):
    if message.chat.type == "private":
        if message.text == "Random cat sticker":
            sti = open('static/s'+ str(random.randint(0 , 20)) + '.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)



if __name__ == '__main__':
    bot.polling(none_stop = True)
