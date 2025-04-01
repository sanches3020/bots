from aiogram import types

kb_start = [
    types.KeyboardButton(text='Играем'),
    types.KeyboardButton(text='Меню')
]


kb_bets = [
    types.InlineKeyboardButton(text="Ставка $5", callback_data="bet_5"),
    types.InlineKeyboardButton(text="Ставка $10", callback_data="bet_10"),
    types.InlineKeyboardButton(text="Ставка $20", callback_data="bet_20"),
    types.InlineKeyboardButton(text="Ставка $50", callback_data="bet_50")
]