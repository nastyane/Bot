from datetime import datetime

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler


# async def send_message_time(bot: Bot, users: set):
#     print("Ну мы пытались")
#     for user in users:
#         print(user)
#         await bot.send_message(chat_id=user, text=f"это просто сообщение для {user}")


# async def send_message_time_middleware(bot: Bot, users: set):
#     for user in users:
#         print(user)
#         await bot.send_message(chat_id=user, text=f"это ytghjcnj сообщение для {user}")


async def parse_time_make_job(
    msg: str,
    state: FSMContext,
    apscheduler: AsyncIOScheduler,
    date_format: str,
    _type: str
):
    
    new_datetime = datetime.strptime(msg, date_format)
    editing_ad = (await state.get_data()).get("editing_ad")

    if _type == "once":
        if editing_ad.id in apscheduler.get_jobs():
            apscheduler.modify_job(id=editing_ad.id, run_date=new_datetime)
        else:
            apscheduler.add_job(
                editing_ad.timed_send,
                trigger="date",
                run_date=new_datetime,
            )

    elif _type == "every_day":
        if editing_ad.id in apscheduler.get_jobs():
            apscheduler.remove_job(editing_ad.id)

        apscheduler.add_job(
            editing_ad.timed_send,
            trigger="cron",
            hour=new_datetime.hour,
            minute=new_datetime.minute,
            max_instances = 10
        )

    elif _type == "intervals":
        if editing_ad.id in apscheduler.get_jobs():
            apscheduler.remove_job(editing_ad.id)

        apscheduler.add_job(
            editing_ad.timed_send,
            trigger="interval",
            hours=new_datetime.hour,
            minutes=new_datetime.minute,
            max_instances = 10
        )
