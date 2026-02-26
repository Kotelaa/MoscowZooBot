import asyncio
import logging

from aiogram import Dispatcher, Router, Bot
from aiogram.filters import Command, CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import types
from aiogram.types import Message
from aiogram.utils.formatting import Bold, as_list, as_marked_list, as_line

from TokenData import TOKEN
from Keyboards import commands_kb, animal_custom_kb


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
    content = as_list(
        Bold('Московский зоопарк 🐾'),
        """Московский зоопарк – один из старейших в Европе, его история 
        началась еще в 1864 году. Основанный профессорами Московского 
        университета, он с первых дней стал не просто местом для прогулок, а 
        важнейшим научным центром. Даже его расположение на Пресне было выбрано 
        не случайно: когда-то здесь среди садов и лугов протекала чистая река, 
        а само место было доступно для всех горожан. Сегодня зоопарк продолжает 
        эти традиции, используя современную айдентику с изображением 
        манула – символа мудрости и скрытой силы природы. 
        Это живой музей под открытым небом, где сохранение редких видов стоит 
        на первом месте: от работы уникального Центра воспроизводства до 
        внедрения строгих экологических стандартов в повседневную жизнь. \n""",
        Bold('✨ Станьте частью нашей семьи!'),
        as_line(
            """Знаете ли вы, что каждый может внести свой личный вклад 
            в сохранение дикой природы? В Московском зоопарке действует 
            программа""",
            Bold('«Возьми животное под опеку»'),
            """. Став опекуном, вы помогаете обеспечивать вашего любимца лучшим 
            рационом и комфортными условиями жизни. Это прекрасная возможность 
            подружиться с любым обитателем – от величественного белого медведя 
            до крошечного геккона. Опекуны получают именную табличку на вольере 
            и возможность навещать своего подопечного в любое время. """
        )
    )
    await message.answer(content.as_html(), reply_markup=animal_custom_kb)


async def start_bot():
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Bot stopped!')

