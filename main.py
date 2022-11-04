import telebot
from telebot import types
from reminder import Reminder

Token = '5368381125:AAGlTGU8xvi1x4kF4qwBsCjvPDs1PJcueAA'

bot = telebot.TeleBot(Token)

glob_rem = Reminder()
@bot.message_handler(commands=['start'])
def start(massage):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Нагадування про дедлайни.')
    but2 = types.KeyboardButton('Власні нагадування.')
    but3 = types.KeyboardButton('Нагадування для інших.')
    but4 = types.KeyboardButton('Нагадування про перерви, розминку, обід.')

    buttons.add(but1, but2, but3, but4)

    bot.send_message(massage.chat.id, f'Привет! {massage.from_user.first_name}', reply_markup=buttons)


@bot.message_handler(content_types=['text'])
def bot_action(massage):
    if massage.chat.type == 'private':
        if massage.text == "Нагадування про дедлайни.":
            bot.send_message(massage.chat.id, '27.11.2022')
        elif massage.text == 'Власні нагадування.':
            reminder_facilities = types.ReplyKeyboardMarkup(resize_keyboard=True)

            fac1 = types.KeyboardButton('Вивести нагадування')
            fac2 = types.KeyboardButton('Видалити Нагадування')
            fac3 = types.KeyboardButton('Додати нагадування')
            fac4 = types.KeyboardButton('Змінити нагадування ')
            reminder_facilities.add(fac1, fac2, fac3, fac4)

            bot.send_message(massage.chat.id, 'Виберіть бажану дію', reply_markup=reminder_facilities)

            @bot.message_handler(content_types=['text'])
            def remind_actions(user_mess):
                if user_mess.text == 'Вивести нагадування':
                    text = glob_rem.sout_del_rem_list()
                    bot.send_message(user_mess.chat.id, text)


bot.polling(none_stop=True)
