import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# توکن ربات را از متغیر محیطی می‌خوانیم
TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """هندلر دستور /start"""
    await update.message.reply_text('سلام! به ربات پیشرفته من خوش آمدید! 🚀')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """هندلر پیام‌های متنی"""
    await update.message.reply_text(f'شما گفتید: {update.message.text}')

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """هندلر خطاهای ربات"""
    print(f"خطا رخ داد: {context.error}")

def main() -> None:
    """اجرای اصلی ربات"""
    # ایجاد اپلیکیشن
    app = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # اضافه کردن هندلر خطاها
    app.add_error_handler(error_handler)

    # اجرای ربات
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()
