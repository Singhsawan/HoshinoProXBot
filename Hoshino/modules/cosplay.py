import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import *

from telegram.ext import run_async


from Hoshino import pbot

url_nsfw = "https://api.waifu.pics/nsfw/"

@pbot.on_message(filters.command("ncosplay"))
async def ncosplay(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text("Sorry you can use this command only in private chat with bot",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Go PM",url=f"https://t.me/{pbot.me.username}?start=True")]
            ]
        ))
    else:
       ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()

       await msg.reply_photo(ncosplay, caption=f"Ncosplay By @{pbot.me.username}")


@pbot.on_message(filters.command("nwaifu"))
async def nwaifu(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text("Sorry you can use this command only in private chat with bot",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Go PM",url=f"https://t.me/{pbot.me.username}?start=True")]
            ]
        ))
    else:
       url = f"{url_nsfw}waifu"
       result = requests.get(url).json()
       img = result["url"]
       await msg.reply_photo(photo=img)




@pbot.on_message(filters.command("nneko"))
async def nneko(_,msg):
    if msg.chat.type != ChatType.PRIVATE:
      await msg.reply_text("Sorry you can use this command only in private chat with bot",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Go PM",url=f"https://t.me/{pbot.me.username}?start=True")]
            ]
        ))
    else:
       url = f"{url_nsfw}neko"
       result = requests.get(url).json()
       img = result["url"]
       await msg.reply_photo(photo=img)
