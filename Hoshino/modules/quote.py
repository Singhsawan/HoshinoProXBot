import requests
from telegram.ext import run_async
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup

from pyrogram import filters

from Hoshino import pbot

from Hoshino.modules.disable import DisableAbleCommandHandler
from Hoshino import dispatcher

url = "https://animechan.xyz/api/random"


@pbot.on_message(filters.command("quote"))
async def quote(update, context):
    msg = update.effective_message
    quot = requests.get(url).json()
    await msg.reply_text(f"Anime: {quot.anime}\nCharacter: {quot.character}\nQuote: {quot.quote}")

