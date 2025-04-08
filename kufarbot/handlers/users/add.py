from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router, cursor, con, scheduler, bot
from aiogram import F
from script.parser import parser_update, parse_website
import json

class FormUrl(StatesGroup):
    url = State()

@router.message(F.text == "Добавить ссылку")
async def handle_start(message: Message, state: FSMContext):
    user_id = message.from_user.id

    cursor.execute("SELECT * FROM MyTable WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if user:
        await message.answer("Вы уже добавили ссылку.")
    else:
        await message.answer("Пожалуйста, отправьте ссылку.")
        await state.set_state(FormUrl.url)

@router.message(FormUrl.url)
async def handle_url(message: Message, state: FSMContext):
    user_id = message.from_user.id
    url = message.text

    await state.update_data(user_id=user_id, url=url)

    task = scheduler.add_job(
        parser_update,
        trigger='interval',
        seconds=60,
        kwargs={'user_id': user_id, 'bot': bot}
    )

    cursor.execute(
        "INSERT INTO MyTable (id, url, id_task) VALUES (?, ?, ?)",
        (user_id, url, task.id)
    )
    con.commit()

    kb_builder = ReplyKeyboardBuilder()
    kb_builder.add(
        KeyboardButton(text="Добавить ссылку"),
        KeyboardButton(text="Удалить ссылку")
    )
    await message.answer(
        "Парсер успешно запущен.",
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )
