import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
import asyncio

from telegram import (ForceReply, InlineKeyboardButton, InlineKeyboardMarkup,
                      Update)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes, MessageHandler, filters)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Type '/options' to see options")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help! (/start)")


async def split_text(text, max_length):
    start = 0
    while start < len(text):
        end = start + max_length
        yield text[start:end]
        start = end
        await asyncio.sleep(0)  # Даем возможность выполниться другим корутинам

    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "hi":
        answer = "hello"
    else:
        # text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet lacinia, nunc mauris tincidunt nisi, nec ultrices ligula metus in lectus."
        max_length = 20
        loop = asyncio.get_running_loop()
        print(loop.is_running())
        async for answer in split_text(text=text, max_length=max_length):
            await context.bot.send_message(chat_id=update.effective_chat.id, text = answer)
            await loop.sleep(0.5) # Даем возможность выполниться другим корутинам
        # answer = "I don't understand you"
        

    
async def options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Midjourney", callback_data="Midjourney"),
            InlineKeyboardButton("ChatGPT", callback_data="ChatGPT"),
        ],
        [InlineKeyboardButton("Help", callback_data="Help")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    
    ans = query.data
    reply = ""
    
    if ans == "Midjourney":
        reply = MJ()
    elif ans == "ChatGPT":
        reply = GPT()
    elif ans == "Help":
        reply = "/help"
    
    await query.edit_message_text(text=f"Selected option: {reply}")
    
def MJ():
    return "generate image"
    
def GPT():
    return "generate text"
    
def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("OPEN AI TOKEN").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("options", options))
    application.add_handler(CallbackQueryHandler(button))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()