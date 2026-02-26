from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton, \
    ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


def commands_kb():
    keyboard = ReplyKeyboardBuilder()
    commands = ['/description',
            '/commands',
            '/help',
            '/about',
            '/contact',
            '/survey']

    for command in commands:
        keyboard.add(KeyboardButton(text=command))
    keyboard.adjust(3)
    return keyboard.as_markup(resize_keyboard=True)


animal_custom_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Узнать больше о опеке',
                          url='https://moscowzoo.ru/about/guardianship/')]])







