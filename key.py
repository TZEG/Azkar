import asyncio
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
import random
from time import sleep
import zikr

azkar = zikr.azkar

# azkar = ["سبحان الله", "الحمد لله", "الله اكبر"]
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.context) -> None:
    await update.message.reply_text(
        "السلام عليكم و رحمه الله و بركاته , بوت الاذكار يهدف الى تذكيرك من حين الى اخر بذكر الله تقبل الله منا و "
        "منكم صالح الاعمال لتحديد وقت البوت اضغط على /time ")


async def time(update: Update, context: ContextTypes.context) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("5 دقائق ", callback_data="1"),
            InlineKeyboardButton("15 دقيقه", callback_data="2"),
            InlineKeyboardButton("30 دقيقه", callback_data="3"),
        ],
        [
            InlineKeyboardButton("1 ساعه", callback_data="4"),
            InlineKeyboardButton("ساعتين", callback_data="5"),
        ],
        [
            InlineKeyboardButton("4 ساعات", callback_data="6"),
            InlineKeyboardButton("8 ساعات", callback_data="7"),
        ],
        [InlineKeyboardButton("يوم واحد", callback_data="8")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("من فضلك اختار الفيصل الزمنى بين الدعاء و الاخر:", reply_markup=reply_markup)


async def send_azkar(update: Update, context: ContextTypes.context) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    while True:
        await query.answer()
        if query.data == "1":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(10)
        if query.data == "2":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(900)
        if query.data == "3":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(1800)
        if query.data == "4":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(3600)
        if query.data == "5":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(7200)
        if query.data == "6":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(14400)
        if query.data == "7":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(28800)
        if query.data == "8":
            await query.message.reply_text(text=random.choice(azkar))
            sleep(86400)


async def help_command(update: Update, context: ContextTypes.context) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5276707692:AAHf_n794VVIax7rGCa4BZWGjpY6iiZdWu0").build()
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(send_azkar))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
