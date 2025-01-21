from telegram.ext import Application, CommandHandler, MessageHandler, filters
from Environment import TOKEN  # Import token từ env.py
from Response import handle_message, start_command  # Import hàm xử lý từ response.py

def main():
    # Tạo bot với token
    application = Application.builder().token(TOKEN).build()

    # Command
    application.add_handler(CommandHandler("start", start_command))

    # Message
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Chạy bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
