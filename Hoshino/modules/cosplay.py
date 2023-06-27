import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import *

from telegram.ext import run_async


from Hoshino import pbot
from Hoshino import dispatcher
from Hoshino.modules.disable import DisableAbleCommandHandler




@pbot.on_message(filters.command("ncosplay"))
async def ncosplay(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      msg.reply_text("Sorry you can use this command only in private chat with bot",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Go PM",url=f"https://t.me/{pbot.me.username}?start=True")]
            ]
        ))
    else:
       ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()

       msg.reply_photo(ncosplay, caption=f"Cosplay By @{pbot.me.username}")
