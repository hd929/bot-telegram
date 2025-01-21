from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.ext._utils.types import HandlerCallback

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.effective_user:
        await update.message.reply_text(f'Chào {update.effective_user.first_name}')
    else:
        print("Lỗi rồi không khởi động được, thử lại sau!")

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in text: 
        return 'Chào'

    return 'Tôi không hiểu?'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        user_message = update.message.text
        response = handle_response(user_message)
        await update.message.reply_text(response)

