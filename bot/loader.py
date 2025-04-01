from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN

dp = Dispatcher()
router = Router()
dp.include_router(router)
bot = Bot(TOKEN)