import telebot
import conf

TOKEN = conf.TOKEN
API_KEY = conf.API_KEY
BASE_URL = conf.BASE_URL


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Help yourself")

@bot.message_handler(commands=['option'])
def echo_options(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.InlineKeyboardButton('Yes', callback_data='yes')
    itembtn2 = telebot.types.InlineKeyboardButton('No', callback_data='no')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Do you want to option?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'yes':
        bot.answer_callback_query(call.id, "You chose Yes")
    elif call.data == 'no':
        bot.answer_callback_query(call.id, "You chose No")

if __name__ == '__main__':
    bot.polling(none_stop=True)
