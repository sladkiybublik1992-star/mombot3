import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context):
    kb = [["Тест"]]
    await update.message.reply_text(
        "Привет! Бот работает 🌸",
        reply_markup=ReplyKeyboardMarkup(kb, resize_keyboard=True)
    )

async def msg(update: Update, context):
    await update.message.reply_text("Я тебя слышу 💛")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, msg))
    app.run_polling()

if __name__ == "__main__":
    main()