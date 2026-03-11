from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

from Keyboards import survey_options_kb
from quiz_questions import QUIZ_QUESTIONS, RESULTS

router_quiz = Router()

class Quiz(StatesGroup):
    asking = State()

@router_quiz.message(Command('survey'))
async def start_survey(message: Message, state: FSMContext):
    await state.set_state(Quiz.asking)
    await state.update_data(current_step=0, scores={'mammals': 0, 'birds': 0, 'reptiles': 0, 'amphibians': 0})
    await handle_survey(message, state)


@router_quiz.message(Quiz.asking)
async def handle_survey(message: Message, state: FSMContext):
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
    survey_result = RESULTS.get(winner)
    await message.answer_photo(
        photo=survey_result.get('image'),
        caption=f"Тест завершен!\n\n{survey_result.get('message')}",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()





