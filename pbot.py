import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

Pbot = Client(
    "Pbot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_INFO_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('SOURCE CODE', url="https://github.com/SpamShield/PyroGramBot")
        ]]
    ) 
@Pbot.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_sticker("CAACAgUAAxkBAAEBcr1hsLH3Nu0-qQpwwWQ7FkF58xnwSgACpAMAAjieoFU-Q-udLfwBUx4E")
    await message.reply_text(
        f""" Hai {message.from_user.mention} am just a pyrogram bot""", 
        disable_web_page_preview=True,
        reply_markup=START_INFO_BUTTON
    )

Pbot.run()
