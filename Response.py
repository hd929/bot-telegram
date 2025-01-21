from telegram import Update
from telegram.ext import ContextTypes
from fuzzywuzzy import fuzz

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.effective_user:
        await update.message.reply_text(f'Chào {update.effective_user.first_name}')
    else:
        print("Lỗi rồi không khởi động được, thử lại sau!")

def handle_response(text: str, update) -> str:
    processed: str = text.lower()
    
    def message(s, ans):
        if fuzz.partial_ratio(processed, s) > 70 and update.effective_user:
            return ans
        return None
    responses = [
        ("xin chào", f"Xin chào {update.effective_user.first_name}")
    ]

    for s, ans in responses:
        res = message(s, ans)
        if res:
            return res
    
    return "Tôi không hiểu"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        user_message = update.message.text
        response = handle_response(user_message, update)
        await update.message.reply_text(response)

