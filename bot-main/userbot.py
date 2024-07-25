import logging
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import SQLiteSession
from conf.config import api_id, api_hash, phone_number

# Logging configuration
logging.basicConfig(level=logging.INFO)

# API ID, API Hash, and phone number
api_id = api_id
api_hash = api_hash
phone_number = phone_number

# Read sensitive words from file
with open('sokinish.txt', 'r', encoding='utf-8') as file:
    content = file.read()
words = content.split()

# Initialize SQLite session and Telegram client
session = SQLiteSession('userbot')
client = TelegramClient(session, api_id, api_hash)

# Check if user is online
async def is_user_online():
    me = await client.get_me()
    full_user = await client.get_entity(me)
    return full_user.status.online if hasattr(full_user.status, 'online') else False

# Event handlers
@client.on(events.NewMessage(pattern=r'(?i)\bkitob\b'))
async def manipulatsiya_handler(event):
    if event.is_private and not await is_user_online():
        await event.reply(file='python asoslari')



salom = ["salom", "hello"]
xol = ["yaxshi", "qonday", "qanday", "qalay", 'qale']
chaqirish = ["ustoz", "domla", "aka", "teacher", 'ustos', "uztoz", "uztos"]
link = ["http://", "https://"]

@client.on(events.NewMessage)
async def sokinish_handler(event):
    if event.sender_id == (await client.get_me()).id:
        return

    if event.is_private and not await is_user_online():
        print(event.is_private)
        if any(sokin in event.raw_text.lower() for sokin in words):
            await event.delete()
            await event.reply("Odobsiz so'z ishlatmang")
        elif any(i in event.raw_text.lower() for i in link):
            await event.reply("menga xar hil xavolalar tashlamang 😡")
        elif any(i in event.raw_text.lower() for i in salom):
            await event.reply("Valaykum salom")
            await event.reply("qanday yordam bera olaman")
        elif any(i in event.raw_text.lower() for i in xol):
            await event.reply("yaxshi raxmat")
            await event.reply("O'zingizchi")
        elif any(i in event.raw_text.lower() for i in chaqirish):
            await event.reply("Labbay nima muammo")
        else:
            await event.reply('Assalomu Alaykum 👋 men hozir bantman 👨‍💻 ishingiz bulsa yozib qoldiring 📝 birozdan keyin javob beraman⏳')

    print(event.is_private)
# Main function to start the client
async def main():
    try:
        await client.start(phone_number)
        print("Userbot is running...")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.disconnect()

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
