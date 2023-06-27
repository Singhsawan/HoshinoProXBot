import requests
from telegram.ext import run_async
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup

from Hoshino import dispatcher
from Hoshino import pbot

from Hoshino.modules.disable import DisableAbleCommandHandler

url = "https://animechan.xyz/api/random"

@run_async
def quote(update, context):
    msg = update.effective_message
    result = requests.get(url).json()
    msg.reply_message(result)

QUOTE_HANDLER = DisableAbleCommandHandler("quote", quote)


dispatcher.add_handler(QUOTE_HANDLER)

__handlers__ = [
    QUOTE_HANDLER
]

__mod_name__ = "Quote"

__help__ = """
*Commands* *:*  

• `/quote`*:* Get random anime quote.
"""

