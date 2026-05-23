from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8921142309:AAF_kYR291USCCmgWcl23JJIUqSPXtNdZbY"

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["💸 WITHDRAW"],
        ["❌ CANCEL"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🤖 Welcome To Real Income Bot",
        reply_markup=reply_markup
    )

# MESSAGE HANDLE
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💸 WITHDRAW":
        await update.message.reply_text(
            "💰 Withdraw Request Send করুন"
        )

    elif text == "❌ CANCEL":
        await update.message.reply_text(
            "❌ Withdraw Cancel Successfully"
        )

# MAIN
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
