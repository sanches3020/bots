import json 
from aiogram.filters import Command 
from loader import router, cursor, admin_id,bot
import random 
from aiogram.types import Message

@router.message(Command('start_game'))
async def handle_start_reg(message: Message):
    user_id = message.from_user.id

    if user_id not in admin_id:
        await message.answer("Нет доступа")
        return
    
    cursor.execute("SELECT * FROM MyTable")
    data = cursor.fetchall() 

    random.shuffle(data)

    for user in data:
        fio = user[0]     
        numbers = user[1]  
        email = user[2]    
        age = user[3]      

        await message.answer(f"ФИО: {fio}, Номер: {numbers}, Email: {email}, Возраст: {age}")

    with open('data/data.json', encoding='utf-8') as file:
        prize = json.loads(file.read())
    text =('Розыгрыш завершен!\n'
         'Поздравляем победителей с победой:\n'
           )
    for i in range(1):
        text += f'{data[i][1]} - {prize[i]}\n'

        for user in data:
            try:
                await bot.send_message(text=text, chat_id = user[0])
            except:
                pass 

        cursor.execute("DELETE FROM MyTable") 
    
    
    cursor.execute("UPDATE MyTable SET status = False")  
    cursor.connection.commit()  
