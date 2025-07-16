import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

pairs = ["EUR/JPY OTC", "EUR/CHF OTC", "BHD/CNY OTC", "AED/CNY OTC"]
signals = ["Up", "Down"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[pair] for pair in pairs]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Choose a currency pair:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text in pairs:
        signal = random.choice(signals)  # (temporary random signal)
        await update.message.reply_text(f"Signal: {signal}")
    else:
        await update.message.reply_text("Tap a currency from the keyboard.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
