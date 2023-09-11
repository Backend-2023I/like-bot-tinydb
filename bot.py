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

    bot.sendMessage(chat_id, "You send me photo!")

def photo(update: Update, context: CallbackContext):

    print(update.message.message_id)
    bot = context.bot
    chat_id = update.message.chat.id

    likes = db.all_likes()
    dislikes = db.all_dislikes()

    like = InlineKeyboardButton(text=f'👍 {likes}', callback_data='like')
    dislike = InlineKeyboardButton(text=f'👎 {dislikes}', callback_data='dislike')

    keyboard = InlineKeyboardMarkup([[like, dislike]])
    photo = update.message.photo[0].file_id
    bot.sendPhoto(chat_id, photo, reply_markup=keyboard)

def main(update: Update, context: CallbackContext):


    query = update.callback_query
    print(query.message.message_id)
    data = query.data

    chat_id = query.message.chat.id

    if data == 'like':
        db.add_like(chat_id)
    if data == "dislike":
        db.add_dislike(chat_id)

    likes = db.all_likes()
    dislikes = db.all_dislikes()

    like = InlineKeyboardButton(text=f'👍 {likes}', callback_data='like')
    dislike = InlineKeyboardButton(text=f'👎 {dislikes}', callback_data='dislike')

    keyboard = InlineKeyboardMarkup([[like, dislike]])

    query.edit_message_reply_markup(reply_markup=keyboard)

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.photo, photo))
dp.add_handler(CallbackQueryHandler(main))

updater.start_polling()
updater.idle()