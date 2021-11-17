from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from os import environ as env


def start(ud: Update, ctx: CallbackContext):
    ud.message.reply_text('Hola')
    
if __name__ == '__main__':
    updater = Updater(env['TOKEN'])
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()





