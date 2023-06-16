from sys import argv
if len(argv) == 1:
    exit()

import telebot
from telebot import types
bot = telebot.TeleBot(argv[1])

@bot.message_handler(commands=['start', 'help'])
def send_info(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Добавить задачу"))
    keyboard.add(types.KeyboardButton("Удалить задачу"))
    keyboard.add(types.KeyboardButton("Список задач"))
    bot.send_message(message.from_user.id, "Hi, I am todoSher =)", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Добавить задачу":
        bot.send_message(message.from_user.id, "Введи задачу:")
        bot.register_next_step_handler(message, get_do)
    elif message.text == "Удалить задачу":
        bot.send_message(message.from_user.id, "Удалил :)")
    elif message.text == "Список задач":
        bot.send_message(message.from_user.id, "Весёлый =)")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id, "Пока")
    else:
        bot.send_message(message.from_user.id, "Не понимаю, что ты хочешь от меня, чел")


def get_do(message):
    do = message.text
    bot.send_message(message.from_user.id, do)
    bot.send_message(message.from_user.id, "Записал...")


bot.polling(none_stop=True, interval=0)
