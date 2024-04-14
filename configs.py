import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "24921874"))
  API_HASH = os.environ.get("API_HASH", "0aed607bea6fe6e021cb99394848e5e4")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7071579616:AAFCxWS9UM7i7rN7TEHXQLXMTgM1uuMSCOI")
  LUFFY_PIC = os.environ.get("LUFFY_PIC", "https://graph.org/file/1c15be412eb886ba1c8e3.jpg")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "TokenFileStore_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001885156063"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "publicearn.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "72a08a81cd78369774a2e181ab8d66c15efcc82f")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5411073064"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://NoMoreLeader:leadernomore@trialfilterdb.c46bglu.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002038423981")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002143529183"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""<b>╭───────────⍟
├◈ ᴍy ɴᴀᴍᴇ : Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ
├◈ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a> 
├◈ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ: <a href=https://t.me/missqueenbotx>𝙈𝙞𝙨𝙨𝙌𝙪𝙚𝙚𝙣𝘽𝙤𝙩 𝙭</a>   
├◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├◈ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pʏᴛʜᴏɴ 𝟹</a>
├◈ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├◈ Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: <a href=https://t.me/missqueenbotx>Fɪʟᴇ Sᴛᴏʀᴇ V𝟹</a>
╰───────────────⍟ </b> 
"""
  ABOUT_DEV_TEXT = f"""
<b>Hɪ I'M <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a>✨\n
ᴛᴀʟᴋ ᴡɪᴛʜ ᴍᴇ : <a href=https://t.me/sonali_sahaibot>Cʟɪᴄᴋ Hᴇʀᴇ</a>
ᴠɪsɪᴛ ᴍʏ ɢɪᴛʜᴜʙ : <a href=https://github.com/sonali1563>Sᴏɴᴀʟɪ's Gɪᴛʜᴜʙ</a>
ᴍʏ Cʜᴀɴɴᴇʟ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/missqueenbotx>𝙈𝙞𝙨𝙨𝙌𝙪𝙚𝙚𝙣𝘽𝙤𝙩 𝙭</a>
ᴍʏ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ғᴏʀ ʏᴏᴜ : <a href=https://t.me/missqueenbotxchat>𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥</a>
</b>
"""
  HOME_TEXT = """<b>
Hello, [{}](tg://user?id={}) 🤍\n
◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ.
◈ I Cᴀɴ Gɪᴠᴇ Yᴏᴜ Dɪʀᴇᴄᴛ Aɴᴅ Bᴀᴛᴄʜ Lɪɴᴋs Jᴜsᴛ Fᴏʀᴡᴀʀᴅ Mᴇ Fɪʟᴇs.

• Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @missqueenbotx
</b>"""

  Helps_data_test = """<b>
⚪️ Hᴏᴡ ᴛᴏ Usᴇ Bᴏᴛ & ɪᴛ's Bᴇɴᴇғɪᴛs?? 👇

• Sᴇɴᴅ ᴍᴇ ᴀɴʏ Fɪʟᴇ & Iᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ Mʏ Dᴀᴛᴀʙᴀsᴇ & Yᴏᴜ ᴡɪʟʟ Gᴇᴛ ᴛʜᴇ Fɪʟᴇ Lɪɴᴋ.

• Bᴇɴᴇғɪᴛs: Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ TᴇʟᴇGʀᴀᴍ Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ ᴏʀ Aɴʏ Cᴏᴘʏʀɪɢʜᴛ Cʜᴀɴɴᴇʟ, Tʜᴇɴ Iᴛs Usᴇғᴜʟ ғᴏʀ Dᴀɪʟʏ Usᴀɢᴇ, Yᴏᴜ ᴄᴀɴ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Fɪʟᴇ & I ᴡɪʟʟ Sᴇɴᴅ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ ᴛᴏ Yᴏᴜ & Cʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ Sᴀғᴇ ғʀᴏᴍ CᴏᴘʏRɪɢʜᴛ Iɴғʀɪɴɢᴇᴍᴇɴᴛ Issᴜᴇ.

⚪️ ғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ <a href=https://t.me/sonali_sahaibot>Sᴏɴᴀʟɪ</a> : <a href=https://t.me/missqueenbotxchat>Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ</a>
 </b>"""
