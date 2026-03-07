import asyncio
import logging

from aiogram import Dispatcher, Router, Bot
from aiogram.filters import Command, CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.formatting import Bold, as_list, as_marked_list, as_line, \
    Italic

from TokenData import TOKEN
from utils import ALL_CONTACTS
from quiz import router_quiz
from Keyboards import commands_kb, animal_custody_kb, phone_kb


router = Router()

@router.message(CommandStart())
async def welcome_message(message: Message):
    """ Welcome message using command /start """
    content = as_list(
        Bold(f'Привет, {message.from_user.full_name}!'),
        'Добро пожаловать в Бот Московского зоопарка!\n',
        Bold('Доступные команды: '),
        as_marked_list(
            '/description',
            '/commands',
            '/help',
            '/about',
            '/contact',
            '/survey',
            marker='🐾  '
        )
    )
    await message.answer(content.as_html(), reply_markup=commands_kb())


@router.message(Command('about'))
async def about_message(message: Message):
    """ Some information about the ZOO using command /about """
    about_zoo = as_list(
        as_line('Мы — один из старейших зоопарков Европы. Наш символ —',
                Bold('манул'),
                ' олицетворяющий скрытую силу и мудрость природы. 🐱'),
        'Это не просто парк для прогулок, а место, где спасают редкие виды '
        'и заботятся о будущем планеты. 🌿')

    about_custody = as_line(
        'Хотите личную дружбу с пандами или белым медведем? В программе ',
        Bold('«Опека»'),
        ' вы помогаете любимому животному и получаете именную табличку на его '
        'вольере. \n ',
        Bold('Помогайте нам оберегать мир природы вместе! ❤️'))

    content = as_list(
        Bold('Московский зоопарк 🐾'),
        Italic('Оазис живой природы с 1864 года'),
        about_zoo,
        '',
        Bold('✨ Станьте хранителем!'),
        about_custody
    )

    await message.answer(content.as_html(), reply_markup=animal_custody_kb)


@router.message(Command('contact'))
async def contact_message(message: Message):
    """ Contact message using command /contact """
    content = as_list(
        *ALL_CONTACTS,
        sep='\n\n'
    )
    await message.answer(content.as_html(), reply_markup=phone_kb)


async def start_bot():
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(router_quiz)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Bot stopped!')

# СОЗДАТЬ ВЕТКУ