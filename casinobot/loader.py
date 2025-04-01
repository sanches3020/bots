from aiogram import Bot,Dispatcher, Router
from config.token import TOKEN
import sqlite3

con = sqlite3.connect('my_database.db')
cursor = con.cursor()

router = Router()
dp = Dispatcher()
dp.include_router(router) 
bot = Bot("")