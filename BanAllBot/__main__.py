from BanAllBot import app,START_IMG,BOT_USERNAME,BOT_NAME,LOG
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 

START_MSG="""
ʜᴇʏ **{}** , ɪ ᴀᴍ {},
I have some interesting plugins you should tru it by click on the Help Button.
Add me in others group to destroy it.
"""
START_BUTTONS=InlineKeyboardMarkup (
      [
      [
         InlineKeyboardButton (text="➕ Add me ➕",url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
      ],
      [
         InlineKeyboardButton (text="Help",callback_data="help_back")
      ]
      ]
)

HELP_MSG="""
**ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs**

⨷ /banall : Ban-All Members in a Group

⨷ /unbanall : Unban all Members in a Group

⨷ /kickall : Kick all Members in a Group

⨷ /muteall : Mute all Members in a Group

⨷ /unmuteall : Unmute all Members in a Group(sᴛɪʟʟ ᴡɪʟʟ ᴛʜᴇ ʟɪsᴛ ɪɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴍᴇᴍʙᴇʀs ʙᴜᴛ ᴀʟʟ ʀᴇsᴛʀɪᴄᴛɪᴏɴs ᴡɪʟʟ ɢᴏ)

⨷/unpinall : Unpin all Messages in a Group.

Maintenance By: [iamuput](https://t.me/iamuput)
"""




@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_photo(
     photo=START_IMG,
     caption=START_MSG.format(msg.from_user.mention,BOT_NAME),
     reply_markup=START_BUTTONS)

@app.on_callback_query(filters.regex("help_back"))
async def help_back(_,callback_query: CallbackQuery):
    query=callback_query.message
    await query.edit_caption(HELP_MSG)    



if __name__ == "__main__":
    LOG.info("started")
    app.run()
