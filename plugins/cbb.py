# Dont Remove Credit
# Update Channel - TitanXBots
# Ask Any Doubt on Telegram - @TitanOwner.

from pyrogram import Client
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚓ ʜᴏᴍᴇ", callback_data="start"),
                        InlineKeyboardButton("⚡ ᴄʟᴏꜱᴇ", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚓ ʜᴏᴍᴇ", callback_data="start"),
                        InlineKeyboardButton("⚡ ᴄʟᴏꜱᴇ", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🧠 ʜᴇʟᴘ", callback_data="help"),
                        InlineKeyboardButton("🔰 ᴀʙᴏᴜᴛ", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("🧑‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ", user_id=5356695781),
                        InlineKeyboardButton("🔐 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/TitanXBots/FileStore-Bot")
                    ],
                    [
                        InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/TitanXBots"),
                        InlineKeyboardButton("🔍 ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/TitanMattersSupport")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
