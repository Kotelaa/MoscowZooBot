# import re
from aiogram.utils.formatting import as_line, TextLink, \
    Bold, as_list, Italic
from aiogram import Router, F
from aiogram.types import Message

utils_router = Router()


ABOUT_ZOO = as_list(
        as_line(
            'Мы — один из старейших зоопарков Европы. Наш символ —',
            Bold('манул'),
            ' олицетворяющий скрытую силу и мудрость природы. 🐱'),
    'Это не просто парк для прогулок, а место, где спасают редкие виды '
    'и заботятся о будущем планеты. 🌿')

ABOUT_CUSTODY = as_line(
        'Хотите личную дружбу с пандами или белым медведем? В программе ',
        Bold('«Опека»'),
        ' вы помогаете любимому животному и получаете именную табличку на его '
        'вольере. \n ',
        Bold('Помогайте нам оберегать мир природы вместе! ❤️'))

HELP_MESSAGE = as_list(
    Bold('🐾 Помощник Московского зоопарка'),
    'Я помогу тебе узнать больше о наших обитателях и сориентироваться в '
    'услугах зоопарка.\n\n',
    Bold('Доступные команды:'),
    '/start – начать общение',
    '/survey – узнать, какое животное тебе подходит',
    '/contact – посмотреть список телефонов и контактов',
    '/help – показать это справочное сообщение',
    '/about – узнать немного о зоопарке',
    '\n',
    Bold('Как пользоваться ботом?'),
    '1. Нажми /survey, чтобы пройти интерактивный тест.',
    '2. В конце ты получишь результат с фото и описанием твоим тотемным животным.',
    '3. Если нужно позвонить в отдел экскурсий или администрацию — используй /contact.',
    '\n',
    Italic('Если у тебя возникли проблемы, попробуй перезапустить бота командой /start.'))


def add_number(name: str, phone : str =None, mail : str =None):
    """ Add a number to the /contact command """
    content = [Bold(f'{name}: ')]
    if phone:
        # clean_phone = re.sub(r'[^\d+]', '', phone)
        content.append(f'{phone}')
        content.append('  ')
    if mail:
        content.append(TextLink(mail, url=f'mail:{mail}'))
    return as_line(*content)


ALL_CONTACTS = [
    add_number('Телефон для справок по льготам, покупке билетов '
               'и другим вопросам посетителей', phone='+7 (495) 775-33-70'),
        add_number('Администрация', mail='zoopark@culture.mos.ru'),
        add_number('Дежурно-диспетчерская служба(по вопросам оповещения)',
                   mail='pcn@culture.mos.ru'),
        add_number('Детский лагерь «ЗооМастерские»',
                   phone='+7 (499) 255-57-63'),
        add_number('Центр воспроизводства', phone='+7 (903) 004-94-25',
                   mail='info@moscowzoo.center'),
        add_number('Волонтерам', mail='VolonterZoo@culture.mos.ru'),
        add_number('Отдел гуманитарных и творческих программ',
                   phone='+7 (499) 255-57-63'),
        add_number('Арт-Зебра', phone='+7 (906) 084-48-41',
                   mail='ArtzebraZoo@culture.mos.ru'),
        add_number('Заказ экскурсий', phone='+7 (499) 255-53-75',
                   mail='education@moscowzoo.ru'),
        add_number('Пресс-служба', mail='SaralievBS@culture.mos.ru'),
        add_number('Клуб Друзей Московского зоопарка (Опекунство)',
                   phone='+7 (962) 971-38-75', mail='zoofriends@moscowzoo.ru'),
        add_number('Сотрудничество, реализация спонсорских '
                   'и благотворительных программ',
                   mail='partnershipzoo@culture.mos.ru')]


@utils_router.message(F.photo)
async def get_photo_id(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer(f"ID твоей картинки:\n<code>{photo_id}</code>",
                         parse_mode="HTML")
    print(f"File ID: {photo_id}")
