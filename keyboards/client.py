from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_menu = KeyboardButton('Меню')
button_create_zakaz = KeyboardButton('Сделать заказ')
button_add_review = KeyboardButton('Оставить отзыв')
button_reviews = KeyboardButton('Отзывы')
button_numbers = KeyboardButton('Телефоны')
button_cancel = KeyboardButton('Отмена')
button_burgeri = KeyboardButton('Бургеры')
button_bulochki = KeyboardButton('Булочки')
button_zakaz_burgeri = KeyboardButton('Заказать бургеры')
button_zakaz_bulochki = KeyboardButton('Заказать булочки')
button_general = KeyboardButton('Главное')

kb_zakaz_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_zakaz_menu = kb_zakaz_menu.add(button_zakaz_burgeri).add(button_zakaz_bulochki).add(button_general)

kb_general = ReplyKeyboardMarkup(resize_keyboard=True)
kb_general = kb_general.add(button_menu).add(button_create_zakaz).row(button_add_review, button_reviews).add(button_numbers)

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu = kb_menu.add(button_burgeri).add(button_bulochki).add(button_general)

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)