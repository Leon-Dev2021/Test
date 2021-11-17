from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, ConversationHandler, MessageHandler, Filters
from os import environ as env
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from random import randrange

chrome_options = ChromeOptions()
chrome_options.binary_location = env['GOOGLE_CHROME_BIN']
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

INPUTI: int = 0
INPUTII: int = 1
#browser: Chrome = Chrome(executable_path = env['CHROMEDRIVER_PATH'], chrome_options = chrome_options)
lista: list = [1,10,20,4]

def start(ud: Update, ctx: CallbackContext):
    ud.message.reply_text('Hola')
    
def initjob(ud: Update, ctx: CallbackContext):
    ud.message.reply_text('Input shorten link.')
    return INPUTI
    
def ident(ud: Update, ctx: CallbackContext):
    shorten: str = ud.message.text
    #browser.get(shorten)
    ud.message.reply_text('type element id.')
    return INPUTII
    
def click(ud: Update, ctx: CallbackContext):
    elemid = ud.message.text
    #button = browser.find_element_by_id(elemid)
    while True:
        #button.click()
        sleep(lista[randrange(0,len(lista))])
    return ConversationHandler.END
    
if __name__ == '__main__':
    updater = Updater(token = env['TOKEN'])
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',start))
    dispatcher.add_handler(ConversationHandler(
        entry_points = [CommandHandler('job',initjob)],
        states = {
            INPUTI: [MessageHandler(Filters.text,ident)],
            INPUTII: [MessageHandler(Filters.text,click)]
        },
        fallbacks = []
    ))
    updater.start_polling()
    updater.idle()







