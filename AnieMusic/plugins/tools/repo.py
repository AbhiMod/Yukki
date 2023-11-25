import asyncio

from pyrogram import filters

import config
from AnieMusic import app
from AnieMusic.misc import SUDOERS
from AnieMusic.utils.formatters import convert_bytes

@app.on_message(filters.command(["repo"]) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.."
    )
    up_r = f"[𝗥𝗘𝗣𝗢](t.me/About_AMBot)"
    sp_c = config.SUPPORT_CHANNEL
    sp_g = config.SUPPORT_CHAT
    ow_i = f"[ᴀᴍʙᴏᴛ](https://t.me/AM_YTBOTT)"

 ##############
 
    text = f""" Lol⌫

    
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎ ᴀᴍʙᴏᴛ:</u>

𝗥𝗘𝗣𝗢 ❥︎ {up_r}

𝗚𝗥𝗢𝗨𝗣 ❥︎ {sp_g}

𝗢𝗪𝗡𝗘𝗥 ❥︎ {ow_i}

    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)