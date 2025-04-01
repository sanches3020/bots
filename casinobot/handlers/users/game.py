from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.data import get_user_balance, update_user_balance, add_user_to_db, user_exists
from loader import *
from keys.key import kb_bets
import random


@router.message(F.text == 'Играем')
async def fun_text(message: Message):
    id_user = message.from_user.id

    if not user_exists(id_user):
        add_user_to_db(id_user)

    slot_symbols = ['🍋', '⭐️', '🍇', '7️⃣']
    result = [random.choice(slot_symbols) for _ in range(3)]
    result_text = ' | '.join(result)

    money_user = get_user_balance(id_user)

    builder = InlineKeyboardBuilder()
    for button in kb_bets:
        builder.add(button)

    builder.adjust(1)

    await message.answer(
        text=f"Ваш баланс: {money_user}\nДелаем ставку? 🎰\nРезультат: {result_text}",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )


@router.callback_query(F.data.startswith('bet'))
async def game(callback: CallbackQuery):
    bet = int(callback.data.split('_')[1])
    id_user = callback.from_user.id
    money_user = get_user_balance(id_user)

    if bet > money_user:
        await callback.answer(text="Недостаточно средств на счету!")
        return

    slot_symbols = ['🍋', '⭐️', '🍇', '7️⃣']
    result = [random.choice(slot_symbols) for _ in range(3)]
    result_text = ' | '.join(result)

    if result.count(result[0]) == 3:
        update_user_balance(id_user, bet * 2)
        response_text = 'Ты выиграл! Баланс увеличен на сумму ставки.'
    else:
        update_user_balance(id_user, -bet)
        response_text = 'Ты проиграл. Баланс уменьшен на сумму ставки.'

    money_user = get_user_balance(id_user)

    await callback.message.edit_text(
        text=f"Ваш баланс: {money_user}\nРезультат: {result_text}\n{response_text}\nДелаем новую ставку?",
        reply_markup=callback.message.reply_markup
    )

    await callback.answer()