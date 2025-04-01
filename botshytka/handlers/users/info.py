from aiogram import F
from aiogram.types import Message
from loader import router

@router.message(F.text == 'Информация')  
async def handle_info(message: Message):
    file_path = 'data/info.txt' 

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            info_text = file.read()
            await message.answer(info_text)
    except FileNotFoundError:
        await message.answer("Информация не найдена. Пожалуйста, проверьте файл.")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {str(e)}")
