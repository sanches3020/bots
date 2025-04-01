from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from loader import router

@router.message(Command('start'))
async def handle_start(message: Message):
 
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.add(KeyboardButton(text='Регистрация'))
    kb_builder.add(KeyboardButton(text='Информация'))

    await message.answer(
        text="Выберите действие:",
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )
