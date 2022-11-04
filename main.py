import telebot
from telebot import types

Token = '5368381125:AAGlTGU8xvi1x4kF4qwBsCjvPDs1PJcueAA'

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start(massage):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Нагадування про дедлайни.')
    but2 = types.KeyboardButton('Власні нагадування.')
    but3 = types.KeyboardButton('Нагадування для інших.')
    but4 = types.KeyboardButton('Нагадування про перерви, розминку, обід.')

    buttons.add(but1, but2, but3, but4)

    bot.send_message(massage.chat.id, f'Привет! {massage.from_user.first_name}', reply_markup=buttons)


bot.polling(none_stop=True)