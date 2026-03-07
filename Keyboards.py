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


animal_custody_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Узнать больше о опеке',
                          url='https://moscowzoo.ru/about/guardianship/')]])


phone_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="📞 Позвонить в зоопарк", url="tel:+74957753370")]])


def survey_options_kb(options):
    keyboard = ReplyKeyboardBuilder()
    for option in options:
        keyboard.add(KeyboardButton(text=option))
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)




