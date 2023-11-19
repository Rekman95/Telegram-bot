import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from opti import api
from telebot import types
from Avto.External_protection import photos as E_P_Photo

bot = telebot.TeleBot(api)


# Главное меню ____________________________________________________________________________________
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):

    keyboard = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton(text="Авто", callback_data="Auto"),
        InlineKeyboardButton(text="Мать-Ребёнок", callback_data="mother_and_child"),
        InlineKeyboardButton(text="Универмаг", callback_data="Department_store"),
        InlineKeyboardButton(text="Техника", callback_data="technique"),
        InlineKeyboardButton(text="Мужская одежда", callback_data="men's_clothing"),
        InlineKeyboardButton(text="Мебель", callback_data="furniture"),
        InlineKeyboardButton(text="Домашний текстиль", callback_data="Home_textiles"),
        InlineKeyboardButton(text="Сумки / Обувь", callback_data="bags_shoes"),
        InlineKeyboardButton(text="Благоустройство дома", callback_data="Home_improvement"),
        InlineKeyboardButton(text="Красота", callback_data="beauty"),
        InlineKeyboardButton(text="Аксессуары для телефона", callback_data="phone_accessories"),
        InlineKeyboardButton(text="Белье", callback_data="linen"),
        InlineKeyboardButton(text="Украшения", callback_data="decoration"),
        InlineKeyboardButton(text="Спорт", callback_data="sport"),
    ]
    keyboard.add(*buttons)

    bot.send_photo(message.chat.id, photo=open('black cat.jpg', 'rb'), caption='Описание фото',
                   reply_markup=keyboard,
                   disable_notification=True, timeout=10)


# Раздел Авто _____________________________________________________________________________________
@bot.callback_query_handler(func=lambda call: call.data == 'Auto')
def auto_handler(call):
    new_photo = open('black cat.jpg', 'rb')
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        InlineKeyboardButton(text="Внешняя защита", callback_data="External_protection"),
        InlineKeyboardButton(text="Автозапчасти", callback_data="Auto_parts"),
        InlineKeyboardButton(text="Интерьер автомобиля", callback_data="car_interior"),
        InlineKeyboardButton(text="Сиденья", callback_data="seats"),
        InlineKeyboardButton(text="Назад", callback_data="back")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)



# ___________________________________________________________

def handle_message(message):
    chat_id = message.chat.id
    photo_index = 0  # индекс текущей отображаемой фотографии

    # Создание инлайн-кнопок
    markup = InlineKeyboardMarkup(row_width=2)
    bottoms = [
        InlineKeyboardButton('Предыдущее фото', callback_data='previous'),
        InlineKeyboardButton('Следующее фото', callback_data='next'),
        InlineKeyboardButton('Назад', callback_data='back_Auto'),
        InlineKeyboardButton('Корзина', callback_data='basket')
    ]

    markup.add(*bottoms)

    bot.edit_message_media(
        media=telebot.types.InputMediaPhoto(open(E_P_Photo[photo_index], 'rb')),
        chat_id=chat_id,
        message_id=message.message_id,
        reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        """ E_P_Photo: External_protection, Photo - Внешняя защита, Фото """
        nonlocal photo_index

        if call.data == 'previous':
            photo_index = (photo_index - 1) % len(E_P_Photo)
        elif call.data == 'next':
            photo_index = (photo_index + 1) % len(E_P_Photo)
        # elif call.data == 'basket':

        # Обновление сообщения с новой фотографией и кнопками
        bot.edit_message_media(
            media=telebot.types.InputMediaPhoto(open(E_P_Photo[photo_index], 'rb')),
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

# Меню / Авто / Внешняя защита ____________________________________________________________________________


# def handle_message(message):
#     chat_id = message.chat.id
#     photo_index = 0  # индекс текущей отображаемой фотографии
#
#     # Создание инлайн-кнопок
#     markup = InlineKeyboardMarkup(row_width=2)
#     bottoms = [
#         InlineKeyboardButton('Предыдущее фото', callback_data='previous'),
#         InlineKeyboardButton('Следующее фото', callback_data='next'),
#         InlineKeyboardButton('Назад', callback_data='back_Auto'),
#         InlineKeyboardButton('Корзина', callback_data='basket')
#     ]
#
#     markup.add(*bottoms)
#
#     bot.edit_message_media(
#         media=telebot.types.InputMediaPhoto(open(E_P_Photo[photo_index], 'rb')),
#         chat_id=chat_id,
#         message_id=message.message_id,
#         reply_markup=markup)
#
#     @bot.callback_query_handler(func=lambda call: True)
#     def callback_query(call):
#         """ E_P_Photo: External_protection, Photo - Внешняя защита, Фото """
#         nonlocal photo_index
#
#         if call.data == 'previous':
#             photo_index = (photo_index - 1) % len(E_P_Photo)
#         elif call.data == 'next':
#             photo_index = (photo_index + 1) % len(E_P_Photo)
#         # elif call.data == 'basket':
#
#         # Обновление сообщения с новой фотографией и кнопками
#         bot.edit_message_media(
#             media=telebot.types.InputMediaPhoto(open(E_P_Photo[photo_index], 'rb')),
#             chat_id=chat_id,
#             message_id=call.message.message_id,
#             reply_markup=markup
#         )


@bot.callback_query_handler(func=lambda call: call.data == 'External_protection')
def auto_External_protection(call):
    handle_message(call.message)


# Меню / Автозапчасти ____________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'Auto_parts')
def Auto_parts(call):
    handle_message(call.message)


# Меню / Интерьер автомобиля ______________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'car_interior')
def auto_car_interior(call):
    handle_message(call.message)


# Меню / Сиденья ____________________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'seats')
def auto_seats(call):
    handle_message(call.message)


# Меню / Назад в Авто _______________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'back_Auto')
def back_Auto(call):
    new_photo = open('black cat.jpg', 'rb')
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Внешняя защита", callback_data="External_protection"),
        types.InlineKeyboardButton(text="Автозапчасти", callback_data="Auto_parts"),
        types.InlineKeyboardButton(text="Интерьер автомобиля", callback_data="car_interior"),
        types.InlineKeyboardButton(text="Сиденья", callback_data="seats"),
        types.InlineKeyboardButton(text="Назад", callback_data="back")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)

# Меню / Корзина ______________________________________________________________________________________________

# @bot.callback_query_handler(func=lambda call: call.data == 'basket')
# def auto_basket(call):
#     handle_message(call.message)

################################################################################################################
################################################################################################################

# Меню / Мать



bot.polling()