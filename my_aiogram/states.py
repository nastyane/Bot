from aiogram.fsm.state import State, StatesGroup


class Gen(StatesGroup):
    text_prompt = State()
    image_prompt = State()
    nothing = State()
    last_message_time = State()
    context = State()

class Bot_advert(StatesGroup):
    ad_new = State()
    ad_choose = State()
    ad_name = State()
    ad_edit = State()
    ad_delete = State()
    ad_edit_info = State()
    ad_edit_timer = State()
    ad_once = State()
    ad_every_day = State()
    ad_intervals = State()
    editing_ad = State()
    start = State()
    only_text = State()
    photo_with_text = State()