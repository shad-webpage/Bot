from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask
import threading
import asyncio

# تنظیمات اولیه
TOKEN = "7868257148:AAEGifr41d3jA_Cvf72sM1BaPWOy4eiFUfM"
WEBHOOK_URL = "آدرس_وبهوک_شما"  # در صورت استفاده از وبهوک
PORT = 8443  # پورت برای وبهوک (اختیاری)

# بخش Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "سرور Flask در حال اجراست! (برای گول زدن سرور اصلی)"

def run_flask():
    app.run(host='0.0.0.0', port=5000)

# بخش Telegram Bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام داش گلم! ربات فعال است.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def run_bot():
    application = Application.builder().token(TOKEN).build()
    
    # دستورات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # اجرای ربات
    application.run_polling()
    # یا برای وبهوک:
    # application.run_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url=WEBHOOK_URL)

if __name__ == "__main__":
    # اجرای Flask در یک ترد جداگانه
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # اجرای ربات تلگرام
    run_bot()
