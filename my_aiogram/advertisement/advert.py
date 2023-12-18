import config
import kb
from admin import users
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

ads = []

class Ad:
    def __init__(self, nm, txt, img, type):
        self.text = txt
        self.image = img
        self.timer = 0
        self.name = nm
        self.type = type
        # ПЕРЕДЕЛАТЬ ОБЯЗАТЕЛЬНО (УДАЛИТЬ первую/добавить ещё 1 и будет 2 одинаковых id)
        self.id = len(ads)
        ads.append(self)

    async def send(self, user):
        if self.type == 1:
            await config.bot.send_photo(
                chat_id=user, caption=self.text, photo=self.image
            )
        elif self.type == 0:
            await config.bot.send_message(
                chat_id=user, text=self.text
            )
        else:
            await config.bot.send_photo(
                chat_id=user, photo=self.image
            )

    async def timed_send(self):
        for _id in users.all_users:
            if self.type == 1:
                await config.bot.send_photo(
                    chat_id=_id, caption=self.text, photo=self.image
                )
            elif self.type == 0:
                await config.bot.send_message(
                    chat_id=_id, text=self.text
                )
            else:
                await config.bot.send_photo(
                    chat_id=_id, photo=self.image
                )

    async def edit(self, text, photo, _type):
        self.type = _type
        self.images = [i for i in photo]
        self.text = text

    async def delete(self):
        ads[ads.index(self)] = None

    def __str__(self):
        return self.text


async def getAdById(_id):
    for ad in ads:
        if ad.id == _id:
            return ad
