import telebot
import sqlite3

bot = telebot.TeleBot('6943016439:AAGveKLxbvtvyqdZpqjmg7G4d7ObT9DdEvw')
name = None # Глобальная переменная

@bot.message_handler(commands=['Sch']) # создаю чат бота
def sch(message):
    conn = sqlite3.connect('itproger.sql') # создаю базу данных и указываю название базы данных
    cur = conn.cursor() # курсор для работы с базой данных

    cur.execute('CREATE TABLE IF NOT EXISTS users '     #'СОЗДАТЬ ТАБЛИЦУ, ЕСЛИ НЕ СУЩЕСТВУЕТ,
                '(id int auto_increment primary key, '  #пользователи, (id число автоизменяется первичного ключа
                'name varchar(50), pass varchar(50))')  #(имя varchar(50), пароль varchar(50))'
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя ')
    bot.register_next_step_handler(message, user_name)  # как только пользователь введёт имя, будет регистрация
                                                        # в функции user_name

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль ')
    bot.register_next_step_handler(message, user_pass) # так же после ввода будет регистрация в функции

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('itproger.sql') # идёт регистрация пользователя
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password)) #ВСТАВИТЬ В пользователей (имя, пароль)
    conn.commit()
    cur.close()
    conn.close() # закрытия базы данных

    markup = telebot.types.InlineKeyboardMarkup() # Создаю кнопку
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users')) # Добавляю кнопку с текстом
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup) # Вывожу сообщение


@bot.callback_query_handler(func=lambda call: True) # Обработка кнопки
def callback(call):
    conn = sqlite3.connect('itproger.sql')  # открытие базы данных
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users") # выбрать все поля из users
    users = cur.fetchall() # это функция вернёт все записи

    info = ''
    for el in users: # в новую строку добовляем информацию имя и пароль и с новой строки
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'

    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling()