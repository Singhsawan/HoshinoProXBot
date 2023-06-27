import requests
from telegram.ext import run_async
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup

from pyrogram import filters

from Hoshino import pbot

url = "https://animechan.xyz/api/random"

@pbot.on_message(filters.command("cosplay"))
async def quote(update, context):
    msg = update.effective_message
    result = requests.get(url).json()
    await msg.reply_message(result)

# QUOTE_HANDLER = DisableAbleCommandHandler("quote", quote)


# dispatcher.add_handler(QUOTE_HANDLER)

# __handlers__ = [
#     QUOTE_HANDLER
# ]

# __mod_name__ = "Quote"

# __help__ = """
# *Commands* *:*  

# • `/quote`*:* Get random anime quote.
# """

