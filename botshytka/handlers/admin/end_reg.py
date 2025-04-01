from aiogram.types import Message 
from aiogram.filters import Command 
from loader import router, cursor, admin_id 

@router.message(Command('end_reg'))
async def handle_end_reg(message: Message):
    user_id = message.from_user.id

    if user_id not in admin_id:
        await message.answer("Нет доступа")
        return

    cursor.execute("UPDATE MyTable SET status = ?", (False,))  
    cursor.connection.commit()  

    await message.answer("Регистрация завершена.")