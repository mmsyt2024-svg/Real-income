from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8921142309:AAF_kYR291USCCmgWcl23JJIUqSPXtNdZbY"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running successfully!")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
