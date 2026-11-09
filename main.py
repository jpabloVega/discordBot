import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

_ = load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Miku bot clean start")

# @bot.event
# async def on_member_join(member):
#    await member.send(f"Saludos a {member.name} y huevos al Desfan")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "huevos" in message.content.lower():
        await message.channel.send("al desfan")

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG )
