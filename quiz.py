from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.utils.formatting import Bold, as_list, as_marked_list

from Keyboards import survey_options_kb, share_keyboard
from quiz_questions import QUIZ_QUESTIONS, RESULTS

DEFAULT_QUIZ_DATA = {
    'current_step': 0,
    'scores': {'mammals': 0, 'birds': 0, 'reptiles': 0, 'amphibians': 0}
}

router_quiz = Router()

class Quiz(StatesGroup):
    asking = State()

@router_quiz.message(Command('survey'))
async def start_survey(message: Message, state: FSMContext):
    """ Function sets the initial state """
    await state.set_state(Quiz.asking)
    await state.update_data(**DEFAULT_QUIZ_DATA)
    await handle_survey(message, state)


@router_quiz.message(Quiz.asking)
async def handle_survey(message: Message, state: FSMContext):
    """ Asks questions about the user's compatibility with different animals """
    data = await state.get_data()
    current_step = data.get('current_step', 0)
    scores = data.get('scores', {'mammals': 0, 'birds': 0, 'reptiles': 0, 'amphibians': 0})

    if current_step > 0:
        prev_question = QUIZ_QUESTIONS[current_step-1]
        user_answer = message.text

        answer_result = prev_question.get('options').get(user_answer)
        if answer_result:
            scores[answer_result] += 1

    if current_step < len(QUIZ_QUESTIONS):
        question_data = QUIZ_QUESTIONS[current_step]
        question = question_data.get('question')
        answers = list(question_data.get('options').keys())
        kb = survey_options_kb(answers)
        await message.answer(question, reply_markup=kb)
        await state.update_data(current_step=current_step+1, scores=scores)

    else:
        winner = max(scores, key=scores.get)
        await show_result(message, state, winner)


async def show_result(message: Message, state: FSMContext, winner: str):
    await message.answer(text='Загружаю результат...',
                         reply_markup=ReplyKeyboardRemove())

    survey_result = RESULTS.get(winner)
    content = as_list(
        f'Тест завершен!',
        f"{survey_result.get('message')}",
        '\n',
        Bold('Станьте ангелом-хранителем!'),
        'Московский зоопарк уже более 160 лет заботится о редких видах. Программа '
        '«Клуб друзей» дает возможность каждому внести вклад в сохранение природы.',
        '\n',
        'Опека — это не просто благотворительность, это особая связь с животным. '
        'Благодаря вашей поддержке мы обеспечиваем наших подопечных лучшими '
        'кормами, игрушками и комфортными вольерами.',
        '\n',
        Bold('Что дает опека?'),
        as_marked_list(
            'Именная табличка на вольере.',
            'Бесплатный вход в зоопарк.',
            'Участие в специальных мероприятиях и встречах.',
            marker='✅ '
        ),
        '\n',
        'Узнать больше об опеке можно по команде /contact или на нашем '
        'официальном сайте. ✨'
    )

    await message.answer_photo(photo=survey_result.get('image'),
                               caption=content.as_html(),
                               reply_markup=share_keyboard(survey_result.get('animal'))
    )
    await state.clear()



