import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from carparktool import CPMNuker

TOKEN = "7370949688:AAHfL92Iowqg22K-Tu4GG-xNWO6RyZhHOgk"

nuker = CPMNuker()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot.")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    await app.run_polling()

if _name_ == "_main_":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(main())
