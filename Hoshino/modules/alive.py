from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

import random

from Hoshino import BOT_NAME, BOT_USERNAME, OWNER_ID, SUPPORT_CHAT, pbot 

START_VID = (
    "https://telegra.ph/file/e374ba92cd333abe12c8a.mp4",
    "https://telegra.ph/file/39a18d24aa651ef6497af.mp4",
    "https://telegra.ph/file/96fed135fe1820925555e.mp4",
    "https://telegra.ph/file/c38a9d63ac2355075a534.mp4",
    "https://telegra.ph/file/ed6111ed26510b0af4357.mp4",
    "https://telegra.ph/file/bbdaf08bbefc3df7f81c9.mp4",
    "https://telegra.ph/file/65df8a4d8df645b9b5be9.mp4",
    "https://telegra.ph/file/dab74ea839ad9ffdfc12b.mp4",
    "https://telegra.ph/file/52241f62d8bc991605e6e.mp4",
    "https://telegra.ph/file/047f6761ebfbf4f6539d2.mp4",
)


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"**ʜᴇʏ {message.from_user.mention},\n\nɪ ᴀᴍ {BOT_NAME}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** [KIRA](tg://user?id={OWNER_ID})\n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    await message.reply_photo(
        photo=random.choice(START_VID),
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


__mod_name__ = "Aʟɪᴠᴇ"
