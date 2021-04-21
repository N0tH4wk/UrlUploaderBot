#    Copyright (c) 2021 Infinity BOTs <https://t.me/Infinity_BOTs>
 
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.


import os
import wget
from pyrogram import filters, Client
from config import Config

# login to pyrogram client
JEBotZ = Client(
   "URL Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@JEBotZ.on_message(filters.command("url") & filters.edited)
async def urlupload(client, message):
    url = message.text.split(None, 1)[1]
    sed = await message.reply("Checking Url 🧐")
    try: # url download via wget
       lel = wget.download(url)
       await message.reply_document(lel)
       sed.delete()
    except Exception: # print error
        sed.edit("Unsupported Url 🙄")
    os.remove(lel) # remove downloaded file from server

print("JEBotZ Started!")

# start bot
JEBotZ.run()
