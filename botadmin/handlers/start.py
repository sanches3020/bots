from aiogram.filters import Command
from aiogram.types import Message
from loader import router

@router.message(Command('start'))
async def start(message: Message):
     await message.answer(text='Добро пожаловать! Я бот-модератор')