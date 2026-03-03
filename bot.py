from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m: Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        await app.send_message(
            kk.id,
            f"**👋 Hello {kk.mention}!\n\n🎉 Welcome to {op.title} 🎉\n\n✅ You are approved automatically!\n💡 Powered by @VJ_Botz**"
        )
        add_user(kk.id)
    except errors.PeerIdInvalid:
        print("user isn't start bot (means group)")
    except Exception as err:
        print(str(err))


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.private & filters.command("start"))
async def start(_, m: Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id)
    except:
        try:
            invite_link = await app.create_chat_invite_link(int(cfg.CHID))
        except:
            await m.reply("**Make Sure I Am Admin In Your Channel**")
            return

        # ─── Inline Buttons 3 Rows ───
        key = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("˹ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ˼", url="")],  # Row 1
                [InlineKeyboardButton("˹ᴏᴡɴᴇʀ˼", url="")],                 # Row 2
                [
                    InlineKeyboardButton("˹ᴜᴘᴅᴀᴛᴇ˼", url=""),               # Row 3, first button
                    InlineKeyboardButton("˹sᴜᴘᴘᴏʀᴛ˼", url="")              # Row 3, second button
                ]
            ]
        )

        # ─── Welcome Message with Image ───
        await m.reply_photo(
            photo="https://files.catbox.moe/dgelfj.jpg",
            caption=f"""**👋 ʜᴇʟʟᴏ {m.from_user.mention}!**
**❍ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴜᴛᴏ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ᴀᴄᴄᴇᴘᴛᴇʀ ʙᴏᴛ. 🥳**
**✦━━━━━━━━━━━━━━━━━━━━━✦**
**🛠 ғᴇᴀᴛᴜʀᴇs :**
**❍ ᴀᴜᴛᴏ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ᴀᴄᴄᴇᴘᴛᴇʀ ɪɴ ɢʀᴏᴜᴘ.**
**❍ ɢɪᴠᴇ ᴛʜᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴏғ ɪɴᴠɪᴛᴇ ʟɪɴᴋ & ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ**
**✦━━━━━━━━━━━━━━━━━━━━━✦**
**➤ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ᴍɪsᴛᴇʀ ꭙ sᴛᴀʀᴋ](https://t.me/CarelessxOwner)**
**➤ ᴍᴏʀᴇ ʙᴏᴛs : [sᴛᴀʀᴋ ꭙ ɴᴇᴛᴡᴏʀᴋ](https://t.me/StarkxNetwrk)**
**➤ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴄᴀʀᴇʟᴇss ꭙ ᴄᴏᴅᴇʀ](https://t.me/ll_CarelessxCoder_ll)**
**╰─━━━ ✦ ❀ ✦ ❖ ✦ ❀ ✦ ━━━─╯**
""",
            reply_markup=key,
            has_spoiler=True
        )
        return

    # User already joined, normal welcome
    keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("˹ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ˼", url="")],  # Row 1
                [InlineKeyboardButton("˹ᴏᴡɴᴇʀ˼", url="")],                 # Row 2
                [
                    InlineKeyboardButton("˹ᴜᴘᴅᴀᴛᴇ˼", url=""),               # Row 3, first button
                    InlineKeyboardButton("˹sᴜᴘᴘᴏʀᴛ˼", url="")              # Row 3, second button
                ]
            ]
        )

    add_user(m.from_user.id)
    await m.reply_photo(
        "https://graph.org/file/d57d6f83abb6b8d0efb02.jpg",
        caption=f"**🦊 Hello {m.from_user.mention}!\nI'm an auto approve [Admin Join Requests](https://t.me/telegram/153) Bot.\nI can approve users in Groups/Channels. Add me to your chat and promote me to admin with add members permission.\n\n__Powered By : @VJ_Botz__**",
        reply_markup=keyboard
    )


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb: CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
    except:
        await cb.answer("🙅‍♂️ You are not joined my channel first join channel then check again. 🙅‍♂️", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("🗯 Channel", url="https://t.me/vj_botz"),
            InlineKeyboardButton("💬 Support", url="https://t.me/vj_bot_disscussion")
        ]]
    )
    add_user(cb.from_user.id)
    await cb.edit_text(
        text=f"**🦊 Hello {cb.from_user.mention}!\nI'm an auto approve [Admin Join Requests](https://t.me/telegram/153) Bot.\nI can approve users in Groups/Channels. Add me to your chat and promote me to admin with add members permission.\n\n__Powered By : @VJ_Botz__**",
        reply_markup=keyboard
    )


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m: Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
📊 Chats Stats
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}`
""")


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = failed = deactivated = blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1
    await lel.edit(f"📢 Broadcast Completed!\n✅ Sent: `{success}`\n❌ Failed: `{failed}`\n🚫 Blocked: `{blocked}`\n💀 Deactivated: `{deactivated}`")


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = failed = deactivated = blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1
    await lel.edit(f"📢 Broadcast Forward Completed!\n✅ Sent: `{success}`\n❌ Failed: `{failed}`\n🚫 Blocked: `{blocked}`\n💀 Deactivated: `{deactivated}`")


print("I'm Alive Now!")
app.run()
