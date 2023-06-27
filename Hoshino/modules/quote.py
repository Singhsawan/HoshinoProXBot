import requests
from telegram.ext import run_async
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup

from pyrogram import filters

from Hoshino import pbot

from Hoshino.modules.disable import DisableAbleCommandHandler
from Hoshino import dispatcher

url = "https://animechan.xyz/api/random"


@run_async
def quote(update, context):
    msg = update.effective_message
    quot = requests.get("https://waifu-api.vercel.app").json()
    msg.reply_text(f"Anime: {quot.anime}\nCharacter: {quot.character}\nQuote: {quot.quote}")




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

