from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# توکن ربات را از متغیر محیطی می‌خوانیم
TOKEN = os.getenv('BOT_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! به ربات ساده من خوش آمدید! 😊')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'شما گفتید: {update.message.text}')

def main():
    # ایجاد آپدیتر و دیسپچر
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # اضافه کردن هندلرها
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
