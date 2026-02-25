import asyncio
import logging

from aiogram import Dispatcher, Router, Bot
from aiogram.filters import Command, CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import types
from aiogram.types import Message
from aiogram.utils.formatting import Bold, as_list, as_marked_list

from TokenData import TOKEN
from Keyboards import commands_kb


router = Router()

@router.message(CommandStart())
async def welcome_message(message: Message):
    content = as_list(
        Bold(f'Привет, {message.from_user.full_name}!'),
        'Добро пожаловать в Бот Московского зоопарка!\n\n',
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


async def main():
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped!')

# СОЗДАТЬ ВЕТКУ