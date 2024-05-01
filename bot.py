import discord
from discord.ext import commands
from discord.ui import Button, View
from session import Session
from commands import *
from player import Player, Mage, Warrior, Ranger
from dotenv import load_dotenv
import os

#load the environment variables
load_dotenv()

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
BOT_TOKEN = os.getenv("BOT_TOKEN")
 # Create a bot instance
bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())
session = Session()


# Event to print a message when the bot is ready
@bot.event
async def on_ready():
    print("Bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Bot is ready")
    

# end the play session after a period of inactivity
@bot.event
async def on_message(message):
    if session.is_active:
        session.start_time = message.created_at.timestamp()
    await bot.process_commands(message)


@bot.command()
async def new_character(ctx):
    view = View()
    if session.player:
        session.player = None
    mage_button = Button(label="Mage", style=discord.ButtonStyle.primary)
    warrior_button = Button(label="Warrior", style=discord.ButtonStyle.primary)
    ranger_button = Button(label="Ranger", style=discord.ButtonStyle.primary)
    
    
    # Define callback functions for the buttons
    async def mage_callback(interaction):
        session.player = Mage(ctx.author.name)
        await interaction.response.send_message(f"You chose Mage!")
        print(session.player)
        
        
    async def warrior_callback(interaction):
        session.player = Warrior(ctx.author.name)
        await interaction.response.send_message(f"You chose Warrior!")
        print(session.player)

        
    async def ranger_callback(interaction):
        session.player = Ranger(ctx.author.name)
        await interaction.response.send_message(f"You chose Ranger!")
        print(session.player.name)
    
    # Assign the callbacks to the buttons
    mage_button.callback = mage_callback
    warrior_button.callback = warrior_callback
    ranger_button.callback = ranger_callback
    
    # Add the buttons to the view
    view.add_item(mage_button)
    view.add_item(warrior_button)
    view.add_item(ranger_button)
    
    # Send a message with the view containing the buttons
    await ctx.send("Choose your class:", view=view)
    

@bot.command()
async def status(ctx):
    #checks if a player exists in session
    if not session.player:
        await ctx.send("No player found. Create a new character with the !new_character command")
        return
    # show the player stats
    player = session.player
    await ctx.send(f"Name: {player.name}\nClass: {player.player_class}\nHealth: {player.health}\nMana: {player.mana}\nLevel: {player.level}")
    
# start the bot
bot.run(BOT_TOKEN)