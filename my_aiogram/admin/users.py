import utils, config
from apscheduler.schedulers.asyncio import AsyncIOScheduler


admins = set([446870226, 171179169])
moderators = set()
all_users = set() | admins | moderators

def isAdmin(user_id):
    return user_id in admins

def isModerator(user_id):
    return user_id in moderators


users_cls = dict()

async def update_limits(apscheduler: AsyncIOScheduler):
    for _, user in users_cls.items():
        user.limit = 30
    apscheduler.add_job(update_limits, trigger="cron", hour=0, minute=0)

# AsyncIOScheduler.add_job(func=update_limits, trigger="cron", hour=0, minute=0)
    

def new_user(user):
    us = User(user.username, user.id)
    users_cls[us.telegram_id] = us

class User:
    def __init__(self, nm = "", telegram_id = 0, previous_prompt="", is_bot=False, active_prompt="", limit:int = 30):
        self.is_bot = is_bot
        self.previous_prompt = previous_prompt
        self.active_prompt = active_prompt
        self.previous_prompt_img = ""
        self.active_prompt_img = ""
        self.username = nm
        self.telegram_id = telegram_id
        self.limit = limit
        self.amount_text_prompts = 0
        self.amount_image_prompts = 0
    
    async def input_prompt_text(self, text):
        self.previous_prompt = self.active_prompt
        self.active_prompt = text
        self.limit -= 1
        self.amount_text_prompts += 1
        await utils.add_request_text()
        print(self.amount_text_prompts, "text prompts for user:", self.username, self.telegram_id)
        # print(self.previous_prompt)
        # print(self.active_prompt)
        
    async def input_prompt_img(self, text):
        self.previous_prompt_img = self.active_prompt_img
        self.active_prompt_img = text
        self.limit -= 1
        self.amount_image_prompts += 1
        await utils.add_request_image()
        print(self.amount_image_prompts, "image prompts for user:", self.username, self.telegram_id)
        # print(self.previous_prompt)
        # print(self.active_prompt)

    async def get_prev_prompt(self):
        return await self.previous_prompt 
    
    