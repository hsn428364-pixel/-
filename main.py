import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# إعدادات البوت
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

# حدث عند بدء البوت
@bot.event
async def on_ready():
    print(f'{bot.user} تم تشغيل البوت بنجاح!')
    try:
        synced = await bot.tree.sync()
        print(f'تم مزامنة {len(synced)} أمر')
    except Exception as e:
        print(e)

# تحميل الأوامر من المجلدات
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'تم تحميل: {filename}')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

import asyncio
if __name__ == '__main__':
    asyncio.run(main())