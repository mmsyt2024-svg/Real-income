from telegram.ext import Updater, CommandHandler

TOKEN = "8921142309:AAF_kYR291USCCmgWcl23JJIUqSPXtNdZbY"


def start(update, context):
    update.message.reply_text("Bot is running successfully ✅")


updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

print("Bot started...")

updater.start_polling()
updater.idle()
