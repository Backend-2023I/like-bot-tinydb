from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, CallbackQueryHandler
from db import LikeDB
import json

db = LikeDB("data.json")

TOKEN ='5892121487:AAFJ8hXhSsCFBNMp-hHqFtAfwhO8RtCxdrM'

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    db.add_student(chat_id)
    bot = context.bot

    bot.sendMessage(chat_id, "Welcome!")

def main(update: Update, context: CallbackContext):
    pass

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CallbackQueryHandler(main))

updater.start_polling()
updater.idle()