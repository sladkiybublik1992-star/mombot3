# main.py — минимальный рабочий бот
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context):
    await update.message.reply_text("Бот работает! 🌸")

async def echo(update: Update, context):
    await update.message.reply_text("Я тебя слышу 💛")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))
    app.run_polling()

if __name__ == "__main__":
    main()

