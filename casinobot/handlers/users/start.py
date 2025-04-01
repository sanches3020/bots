from aiogram import Bot
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types
from aiogram import F
from loader import router
from data.data import get_user_balance, add_user_to_db, user_exists


@router.message(Command('start'))
async def fun_start(message: Message, bot: Bot):
    id_user = message.chat.id

    if not user_exists(id_user):
        add_user_to_db(id_user)

    money_user = get_user_balance(id_user)

    kb_start = ReplyKeyboardBuilder()
    kb_start.add(types.KeyboardButton(text='Играем'))
    kb_start.add(types.KeyboardButton(text='Меню'))

    await message.answer(
        text=f'Добро пожаловать!\nВаш баланс: {money_user}\nВыберите действие:',
        reply_markup=kb_start.as_markup(resize_keyboard=True)
    )

@router.message(F.text == 'Играем')
async def start_game(message: Message):
    id_user = message.from_user.id
    money_user = get_user_balance(id_user)

    bet_buttons = [
        InlineKeyboardButton(text="Ставка $5", callback_data="bet_5"),
        InlineKeyboardButton(text="Ставка $10", callback_data="bet_10"),
        InlineKeyboardButton(text="Ставка $20", callback_data="bet_20"),
        InlineKeyboardButton(text="Ставка $50", callback_data="bet_50"),
    ]

    bet_builder = InlineKeyboardMarkup(inline_keyboard=[bet_buttons])

    await message.answer(
        text=f'Выберите ставку:\nВаш баланс: {money_user}',
        reply_markup=bet_builder
    )