# https://pypi.org/project/CurrencyConverter/

import telebot
from currency_converter import CurrencyConverter
from telebot import types
amount = 0

bot = telebot.TeleBot('6943016439:AAGveKLxbvtvyqdZpqjmg7G4d7ObT9DdEvw')
currency = CurrencyConverter()

@bot.message_handler(commands=['Sch'])
def Sch(message):
    bot.send_message(message.chat.id, 'Привет введите сумму:')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try: # Если amount не целое число, будет повтор запроса
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0: # Если число меньше 0, будет повтор запроса
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR'),
            types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD'),
            types.InlineKeyboardButton('USD/GBP', callback_data='USD/GBP'),
            types.InlineKeyboardButton('Другое значение', callback_data='else')
        ]
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0, впишите новую сумму')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Помлучается: {round(res, 2)}. Можете заново заново вписать сумму')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через "/" ')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Помлучается: {round(res, 2)}. Можете заново заново вписать суммую')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Что-то не так, впишите значение заново')
        bot.register_next_step_handler(message, summa)



bot.polling()