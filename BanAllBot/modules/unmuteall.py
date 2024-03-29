from BanAllBot import app,BOT_ID,SUDO
from pyrogram import filters,enums
from pyrogram.types import ChatPermissions 

@app.on_message(filters.command("unbisu") & filters.user(SUDO))
async def unmute_all(_,msg):
    chat_id=msg.chat.id   
    x = 0
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True 
    if bot_permission:
        banned_users = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
            banned_users.append(m.user.id)       
            try:
                    await app.restrict_chat_member(chat_id,banned_users[x], ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_polls=True,can_add_web_page_previews=True,can_invite_users=True))
                    
                    x += 1
                                        
            except Exception as e:
                print(e)
    else:
        await msg.reply_text("Either i don't have the right to restrict users or you are not in sudo users")  
