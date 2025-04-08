from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router

@router.message(Command('start'))
async def handle_start(message: Message):

    kb_builder = ReplyKeyboardBuilder()
    kb_builder.add(
        KeyboardButton(text='Добавить ссылку'),
        KeyboardButton(text='Удалить ссылку')
    )

    await message.answer(
        "Добро пожаловать! Выберите действие:",
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )
