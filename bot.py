import discord
from discord.ext import commands
from cogs.session import Session
from dotenv import load_dotenv
import os
import asyncio

# Load the environment variables from config.env
load_dotenv("config.env")

CHANNEL_ID = os.getenv("CHANNEL_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

 # Create a bot instance
bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())
session = Session()

'''
# Event to print a message when the bot is ready
@bot.event
async def on_ready():
    print("Bot is ready")
    channel = bot.get_channel(int(os.getenv("CHANNEL_ID")))
    if channel is not None:
        await channel.send("Bot is ready")
    else:
        print("Channel is None")
    

# end the play session after a period of inactivity
@bot.event
async def on_message(message):
    if session.is_active:
        session.start_time = message.created_at.timestamp()
'''

# load the cogs
async def load_cogs():
    for file in os.listdir('./cogs'):
        if file.endswith(".py"):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load_cogs()
    await bot.start(BOT_TOKEN)

# start the bot
asyncio.run(main())