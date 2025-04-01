from aiogram.types import Message 
from aiogram.filters import Command 
from loader import router, cursor, admin_id 


@router.message(Command('start_reg'))
async def handle_start_reg(message: Message):
    user_id = message.from_user.id

    if user_id not in admin_id:
        await message.answer("Нет доступа")
        return

    cursor.execute("DELETE FROM start_reg")  
    cursor.execute("INSERT INTO start_reg (status) VALUES (?)", (True,))
    cursor.connection.commit()

    await message.answer("Регистрация запущена.")