import requests
from telegram.ext import run_async
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup

from pyrogram import filters

from Hoshino import pbot


url = "https://animechan.xyz/api/random"


@pbot.on_message(filters.command("quote"))
async def quote(update, context):
    quot = requests.get(url).json()
    await context.reply_text(f"Anime: {quot.anime}\nCharacter: {quot.character}\nQuote: {quot.quote}")

