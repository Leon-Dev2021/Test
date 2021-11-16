from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler


def start(ud: Update, ctx: CallbackContext):
    ud.message.reply_text('Hola')
    
if __name__ == '__main__':
    updater = Updater('1810373040:AAHBEoOG1h4FxZ4QCzRfAIo9g9P24DF3F2w')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()





