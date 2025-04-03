from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN

FORBIDDEN_WORDS =[
    'спам',
    'реклама',
    'взлом',
]

user_violations = {}
MAX_VIOLATIONS = 3
MUTE_VIOLATIONS = 5
dp = Dispatcher()
router = Router()
dp.include_router(router)
bot = Bot(TOKEN)