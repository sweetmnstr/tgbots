import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(context_types = ["text"] )
def exo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(non_stop = True)
