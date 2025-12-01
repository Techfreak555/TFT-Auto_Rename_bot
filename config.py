import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 



# Fetch initial admin list
ADMIN = []  # TemporLoad admins when the bot starts

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "9911380")
    API_HASH  = os.environ.get("API_HASH", "b9d1a9112401026acdfc094dc63394ac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7605765172:AAFZo1kENMCT8v8o3BH2UZJfY5DB-YKoC9Y") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Agastin")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Agastin:U3sy2yPCqZW5evMi@cluster0.zvjb81i.mongodb.net/?appName=Cluster0")
    PORT = os.environ.get("PORT", "8050")
    OWNER = int(os.environ.get("OWNER", "6290450484"))
    PRIVATE_USE = False #If Bot is private use set True otherwise False
 
    # other configs
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/cad6d11a62a0d7bea2671-45849ed0a2355b53e4.jpg")
    
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', "allanimetamil177").split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "" ))
    DUMB_CHANNEL = os.environ.get("DUMB_CHANNEL", "")
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 👋 

<blockquote>➻ This Is An Advanced Auto rename Bot.

➻ Using This Bot You Can Able to Rename Your Files one by one or multi.

➻ You Can Also Select the file type is need to upload.

<blockquote><b>Bot Is Made By :</b> @allanimetamil177</blockquote>"""

    ABOUT_TXT = f"""<blockquote><b>😈 My Name :</b> <a href='https://t.me/Tech_Freak_Tamil'>Auto Renamer bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Tech_Freak_Tamil'>TFT BOTS</a>
<b>🛡️ Disscussion :</b> <a href='https://t.me/+ov2l_dY_8jA3MGVl'>TFT Discussion</a></blockquote>
    
<blockquote><b>😈 Bot Made By :</b> <a href='https://t.me/+ov2l_dY_8jA3MGVl'>TFT Discussion</a></blockquote>"""

    HELP_TXT = """<blockquote>
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /settings - Set Queue, Upload type and metadata 
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

</blockquote>"""

    PROGRESS_BAR = """\n<blockquote>
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
</blockquote>"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `Now off❌`
"""


    SEND_METADATA = """<blockquote><b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @Tech_Freak_Tamil</code>

💬 For Any Help Contact @Tech_Freak_Tamil
</blockquote>"""


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Tech_freak_tamil
# Developer @devilo7


