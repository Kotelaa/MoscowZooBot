from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton, \
    ReplyKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardMarkup


# В чем разница ReplyKeyboardBuilder и KeyboardBuilder
def commands_kb():
    kb = ReplyKeyboardBuilder()
    commands = ['/description',
            '/commands',
            '/help',
            '/about',
            '/contact',
            '/survey']

    for command in commands:
        kb.add(KeyboardButton(text=command))
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)





