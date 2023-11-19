import telebot
from telebot import types
from opti import api

bot = telebot.TeleBot(api)

list_photo = ['Avto/External protection/Cat with headphones.jpg',
          'Avto/External protection/Husky.jpg',
          'Avto/External protection/Leopard.jpg',
          'Avto/External protection/white tiger cub.jpg']

# photo_index = 0

@bot.message_handler(commands=['Sch'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text="Авто", callback_data="Auto"),
        types.InlineKeyboardButton(text="Мать-Ребёнок", callback_data="mother_and_child"),
        types.InlineKeyboardButton(text="Универмаг", callback_data="Department_store"),
        types.InlineKeyboardButton(text="Техника", callback_data="technique"),
        types.InlineKeyboardButton(text="Мужская одежда", callback_data="men's_clothing"),
        types.InlineKeyboardButton(text="Мебель", callback_data="furniture"),
        types.InlineKeyboardButton(text="Домашний текстиль", callback_data="Home_textiles"),
        types.InlineKeyboardButton(text="Сумки / Обувь", callback_data="bags_shoes"),
        types.InlineKeyboardButton(text="Благоустройство дома", callback_data="Home_improvement"),
        types.InlineKeyboardButton(text="Красота", callback_data="beauty"),
        types.InlineKeyboardButton(text="Аксессуары для телефона", callback_data="phone_accessories"),
        types.InlineKeyboardButton(text="Белье", callback_data="linen"),
        types.InlineKeyboardButton(text="Украшения", callback_data="decoration"),
        types.InlineKeyboardButton(text="Спорт", callback_data="sport"),
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
        types.InlineKeyboardButton(text="Внешняя защита", callback_data="External_protection"),
        types.InlineKeyboardButton(text="Автозапчасти", callback_data="Auto_parts"),
        types.InlineKeyboardButton(text="Интерьер автомобиля", callback_data="car_interior"),
        types.InlineKeyboardButton(text="Сиденья", callback_data="seats"),
        types.InlineKeyboardButton(text="Назад", callback_data="back")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)


# Авто / Внешняя защита _______________________________________________________________________________________________


# @bot.callback_query_handler(func=lambda call: call.data == 'External_protection')
# def External_protection(call):
#     new_photo = open('Avto/External protection/Husky.jpg', 'rb')
#
#
#
#
#     new_caption = 'Новое описание фото'
#
#     new_keyboard = types.InlineKeyboardMarkup(row_width=2)
#     new_buttons = [
#         types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
#         types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
#         types.InlineKeyboardButton(text="Назад", callback_data="back1"),
#         types.InlineKeyboardButton(text="Корзина", callback_data="basket")
#     ]
#     new_keyboard.add(*new_buttons)
#
#     bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                            media=types.InputMediaPhoto(media=new_photo, caption=new_caption),
#                            reply_markup=new_keyboard)


# Авто / Внешняя защита / Предыдущее __________________________________________________________________________________

def handle_message(message):
    chat_id = message.chat.id
    photo_index = 0  # индекс текущей отображаемой фотографии

    # Создание инлайн-кнопок
    markup = types.InlineKeyboardMarkup(row_width=2)
    bottoms = [
        types.InlineKeyboardButton('Предыдущее фото', callback_data='previous'),
        types.InlineKeyboardButton('Следующее фото', callback_data='next'),
        types.InlineKeyboardButton('Назад', callback_data='back_Auto'),
        types.InlineKeyboardButton('Корзина', callback_data='basket')
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


@bot.callback_query_handler(func=lambda call: call.data == 'External_protection')
def auto_handler(call):
    handle_message(call.message)


# @bot.callback_query_handler(func=lambda call: True)
# def External_protection_tovar(call):
#     global photo_index
#
#     if call.data == 'back_product':
#         photo_index = (photo_index - 1) % len(list_photo)
#     elif call.data == 'Next_product':
#         photo_index = (photo_index + 1) % len(list_photo)
#
#     new_caption = 'Новое описание фото'
#
#     new_keyboard = types.InlineKeyboardMarkup(row_width=2)
#     new_buttons = [
#         types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
#         types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
#         types.InlineKeyboardButton(text="Назад", callback_data="back1"),
#         types.InlineKeyboardButton(text="Корзина", callback_data="basket")
#     ]
#     new_keyboard.add(*new_buttons)
#
#     bot.edit_message_media(chat_id=call.message.chat.id,
#                            message_id=call.message.message_id,
#                            media=types.InputMediaPhoto(media=list_photo, caption=new_caption),
#                            reply_markup=new_keyboard)


# Авто / Автозапчасти ________________________________________________________________________________________________


@bot.callback_query_handler(func=lambda call: call.data == 'Auto_parts')
def Auto_parts(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)


# Авто / Интерьер автомобиля   _______________________________________________________________________________________


@bot.callback_query_handler(func=lambda call: call.data == 'car_interior')
def Auto_parts(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)


# Авто / Сиденья  ____________________________________________________________________________________________________


@bot.callback_query_handler(func=lambda call: call.data == 'seats')
def Auto_parts(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)


# Авто / Внешняя защита  <-- Кнопка назад   __________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'back1')
def avto_handler(call):
    new_photo = open('black cat.jpg', 'rb')  # Путь к новому фото
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


# Главное меню <-- Кнопка назад, главное меню  _____________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'back')
def auto_handler(call):
    new_photo = open('black cat.jpg', 'rb')  # Путь к новому фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text="Авто", callback_data="Auto"),
        types.InlineKeyboardButton(text="Мать-Ребёнок", callback_data="mother_and_child"),
        types.InlineKeyboardButton(text="Универмаг", callback_data="button3"),
        types.InlineKeyboardButton(text="Техника", callback_data="button4"),
        types.InlineKeyboardButton(text="Мужская одежда", callback_data="button5"),
        types.InlineKeyboardButton(text="Мебель", callback_data="button6"),
        types.InlineKeyboardButton(text="Домашний текстиль", callback_data="button7"),
        types.InlineKeyboardButton(text="Сумки / Обувь", callback_data="button8"),
        types.InlineKeyboardButton(text="Благоустройство дома", callback_data="button9"),
        types.InlineKeyboardButton(text="Красота", callback_data="button9"),
        types.InlineKeyboardButton(text="Аксессуары для телефона", callback_data="button9"),
        types.InlineKeyboardButton(text="Белье", callback_data="button9"),
        types.InlineKeyboardButton(text="Украшения", callback_data="button9"),
        types.InlineKeyboardButton(text="Спорт", callback_data="button9"),
    ]
    new_keyboard.add(*buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)


# Мать - ребёнок _________________________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'mother_and_child')
def avto_handler(call):
    new_photo = open('black cat.jpg', 'rb')
    new_caption = 'Новое описание фото'
    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Игрушки", callback_data="toys"),
        types.InlineKeyboardButton(text="Перемещение/Коляски", callback_data="travel_strollers"),
        types.InlineKeyboardButton(text="Детские кресла", callback_data="Child_seats"),
        types.InlineKeyboardButton(text="Новинка Осень/Зима", callback_data="New_Autumn_Winter"),
        types.InlineKeyboardButton(text="Детская одежда", callback_data="baby_clothes"),
        types.InlineKeyboardButton(text="Уход за детьми", callback_data="Care_for_children"),
        types.InlineKeyboardButton(text="Зона для беременных", callback_data="Maternity_area"),
        types.InlineKeyboardButton(text="Подгузники/Салфетки", callback_data="Diapers_Wipes"),
        types.InlineKeyboardButton(text="Детская обувь", callback_data="Children's_shoes"),
        types.InlineKeyboardButton(text="Кормление ребёнка", callback_data="Feeding_the_baby"),
        types.InlineKeyboardButton(text="Объёмная одежда", callback_data="Voluminous_clothes"),
        types.InlineKeyboardButton(text="Назад", callback_data="back")
    ]
    new_keyboard.add(*new_buttons)
    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)

# google: conversation telegram bot ,
# postgresql лучше чем sql lite
# docker, docker-compose


# Мать - Ребёнок / Игрушки _________________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'toys')
def avto_handler(call):
    new_photo = open('black cat.jpg', 'rb')  # Путь к новому фото
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


# Мать - Ребёнок / Перемещение и коляски ____________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'travel_strollers')
def travel_strollers(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)



# Мать - Ребёнок / Детские кресла  _________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'Child_seats')
def Child_seats(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)



# Мать - Ребёнок / Новинка Осень и Зима"  _____________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'New_Autumn_Winter')
def New_Autumn_Winter(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)


# Мать - Ребёнок / Детская одежда   ________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'baby_clothes')
def baby_clothes(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)



# Мать - Ребёнок / Уход за детьми  __________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'Care_for_children')
def Care_for_children(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)



# Мать - Ребёнок / Уход за детьми  __________________________________________________________________________________

@bot.callback_query_handler(func=lambda call: call.data == 'Care_for_children')
def Care_for_children(call):
    new_photo = open('Avto/External protection/Husky.jpg', 'rb')  # изменить путь к фото
    new_caption = 'Новое описание фото'

    new_keyboard = types.InlineKeyboardMarkup(row_width=2)
    new_buttons = [
        types.InlineKeyboardButton(text="Предыдущее", callback_data="back_product"),
        types.InlineKeyboardButton(text="Следующее", callback_data="Next_product"),
        types.InlineKeyboardButton(text="Назад", callback_data="back1"),
        types.InlineKeyboardButton(text="Корзина", callback_data="basket")
    ]
    new_keyboard.add(*new_buttons)

    bot.edit_message_media(chat_id=call.message.chat.id, message_id=call.message.message_id,
                           media=types.InputMediaPhoto(media=new_photo, caption=new_caption), reply_markup=new_keyboard)



bot.polling()