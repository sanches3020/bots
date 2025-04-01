from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from loader import router, cursor, con
from aiogram import F

class Form_reg(StatesGroup):
    fio = State()
    numbers = State()
    email = State()
    age = State()

@router.message(F.text == 'Регистрация')
async def start_reg_fun(message: Message, state: FSMContext):
    id_user = message.from_user.id

    cursor.execute("SELECT * FROM MyTable WHERE id = ?", (id_user,))
    user = cursor.fetchone()

    if user:
        await message.answer("Вы уже зарегистрированы.")
        return

    cursor.execute("SELECT status FROM start_reg")
    status = cursor.fetchone()  

    if status and not status[0]:
        await message.answer("Регистрация завершена.")
        return

    await state.set_state(Form_reg.fio)
    await message.answer('Для начала введите ФИО', reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.fio)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await state.set_state(Form_reg.age)
    await message.answer('А теперь введи свой возраст')

@router.message(Form_reg.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Form_reg.numbers)
    await message.answer('А теперь введи свой номер телефона')

@router.message(Form_reg.numbers)
async def get_numbers(message: Message, state: FSMContext):
    await state.update_data(numbers=message.text)
    await state.set_state(Form_reg.email)
    await message.answer('А теперь введи свой email')

@router.message(Form_reg.email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()
    fio = data['fio']
    age = data['age']
    numbers = data['numbers']
    email = data['email']
    user_id = message.chat.id
    cursor.execute("INSERT INTO MyTable (id, fio, age, numbers, email) VALUES (?, ?, ?, ?, ?)",
                   (user_id, fio, age, numbers, email))
    con.commit()
    await message.answer('Регистрация успешна! Добро пожаловать, {}!'.format(fio))
    await state.clear()