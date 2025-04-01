import logging
import asyncio 
from loader import * 

import handlers.users.game
import handlers.users.start
 
async def main(): 
    await dp.start_polling(bot,allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':  
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())