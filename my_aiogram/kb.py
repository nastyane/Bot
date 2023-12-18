from advertisement import advert
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text")],
    [
        InlineKeyboardButton(
            text="🖼 Генерировать изображение", callback_data="generate_image"
        )
    ],
    # [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    # InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    # [InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
    # InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")],
    # [InlineKeyboardButton(text="Рекламка", callback_data="advert")],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

avdert_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Рекламка", callback_data="advert")]]
)
# exit_kb = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True
# )

not_subscribed_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подписаться", url="https://t.me/+tCiKcaWT8nlmNDcy"
            )
        ],
        [InlineKeyboardButton(text="✅ Готово", callback_data="done")],
    ]
)

exit_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]
    ]
)

ad_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="new", callback_data="ad_new"),
            InlineKeyboardButton(text="edit", callback_data="ad_edit"),
        ],
        [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")],
    ]
)


def ad_choose_kb():
    ad_choose_kb1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=ad.name, callback_data=str(ad.id))
                for ad in advert.ads
                if ad != None
            ]
            + [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]
        ]
    )
    return ad_choose_kb1


ad_edit_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отправить себе", callback_data="ad_send")],
        [
            InlineKeyboardButton(
                text="Редактировать текст", callback_data="ad_edit_info"
            ),
            InlineKeyboardButton(
                text="Установить таймер отправки", callback_data="ad_edit_timer"
            ),
        ],
        [InlineKeyboardButton(text="Удалить", callback_data="ad_delete")],
        [InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")],
    ]
)

ad_timer_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Одноразово", callback_data="ad_once"),
            InlineKeyboardButton(text="Каждый день", callback_data="ad_every_day"),
        ],
        [
            InlineKeyboardButton(
                text="Через определённые промежутки", callback_data="ad_intervals"
            )
        ],
    ]
)

# builder = InlineKeyboardBuilder()
# for i in range(15):
#     builder.button(text=f"Кнопка {i}", callback_data=f"button_{i}")
# builder.adjust(2)
# await msg.answer("Текст сообщения", reply_markup=builder.as_markup())
