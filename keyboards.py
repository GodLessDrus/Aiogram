from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
bs = KeyboardButton('/help')
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('picture')
b4 = KeyboardButton('/mult')
kb1.add(bs)
kb.add(b1, b2, b3, b4)


kb_pic = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Картинка')
bp2 = KeyboardButton(text='Главное меню')
kb_pic.add(bp1,bp2)

ibtp = InlineKeyboardMarkup(row_width=2)
ibp1 = InlineKeyboardButton(text='👍',
                            callback_data='like')
ibp2 = InlineKeyboardButton(text='👎',
                            callback_data='dislike')
ibp3 = InlineKeyboardButton(text='➡️',
                            callback_data='next')
ibp4 = InlineKeyboardButton(text='Главное меню',
                            callback_data='main')
ibtp.add(ibp1, ibp2, ibp3,ibp4)