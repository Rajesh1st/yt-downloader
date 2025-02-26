from pyrogram import Client, filters
from pyrogram.handlers import StopPropagation  # ✅ Correct import
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support Channel", url="https://t.me/InFoJosTel")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/InFoJosTelGroup")]
    ])
    welcomed = f"Hi! <b>{message.from_user.first_name}</b>\n/help lo thawn la aw, Min hmandan tur i hriat duh chuan."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
