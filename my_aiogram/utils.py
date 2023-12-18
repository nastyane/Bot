import time

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import Bot_advert, Gen

GRAMMA = (
    {i: "секунд" for i in range(5, 10)}
    | {i: "секунды" for i in range(2, 5)}
    | {1: "секунду", 0: "секунд"}
)

WAIT_CONST = 10
amount_requests = [0, 0]


async def add_request_text():
    amount_requests[0] += 1
    print("all text requests:", amount_requests[0])


async def add_request_image():
    amount_requests[1] += 1
    print("all image requests:", amount_requests[1])


async def split_text(text: str, max_length: int):
    start = 0
    real_end=0
    lenght = len(text)
    while (start < lenght and real_end != -1) and (start + max_length <= lenght):
        end = start + max_length
        real_end = text[start:end].rfind(" ")
        if real_end != -1:
            real_end += start
        else:
            real_end = end
        if text[start:real_end+1]:
            yield text[start:real_end+1]

        # print(start, end, real_end, text[start:real_end+1])   

        start = real_end + 1 
    
    if start <= lenght-1:
        # print("flag")
        yield text[start:]
    

        # await asyncio.sleep(0)  # Даем возможность выполниться другим корутинам


async def check_flood(message: Message, state: FSMContext):
    last_message_time = await state.get_data()
    last_message_time = last_message_time.get("last_message_time", 0)
    # print(last_message_time)

    if last_message_time == None:
        last_message_time = 0

    if last_message_time:
        time_diff = time.time() - float(last_message_time)
        if time_diff < WAIT_CONST:
            # Если время между сообщениями меньше 5 секунд, выводим сообщение о флуде
            await message.reply(
                f"Вы отправляете сообщения слишком часто. Подождите еще {int(WAIT_CONST - time_diff + 1)} {GRAMMA.get(int(WAIT_CONST - time_diff+1)%10)}"
            )
            return True

    # Сохраняем время последнего сообщения пользователя
    await state.update_data(last_message_time=time.time())
    return False


async def check_advert(msg: Message, state: FSMContext):
    if msg.caption != None:
        return 1
    elif msg.text != None:
        return 0
    else:
        return -1
