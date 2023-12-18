import asyncio
import logging
from datetime import datetime, timedelta

import config
from advertisement import apshed
from aiogram import Bot, Dispatcher 
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.chat_action import ChatActionMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers import router
from middleware.advmiddleware import SchedulerMiddleware

async def main():
    config.bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.start()
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    dp.message.middleware(ChatActionMiddleware())
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    await config.bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(config.bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())