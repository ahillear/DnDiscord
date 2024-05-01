from datetime import timedelta, datetime
from discord.ext import commands
from session import Session
from player import Player
import discord

import session, bot

# Commands to start and stop the play session
@bot.command()
async def play(ctx):
    if session.is_active:
        await ctx.send("Session is already active")
    else:
        session.is_active = True
        session.start_time = ctx.message.created_at.timestamp()
        await ctx.send("Session started")

@bot.command()
async def stop(ctx):
    if session.is_active:
        session.is_active = False
        end_time = ctx.message.created_at.timestamp()
        duration = end_time - session.start_time
        human_readable_duration = str(datetime.timedelta(seconds=duration))
        await ctx.send(f"Session stopped after {human_readable_duration}")
    else:
        await ctx.send("No active session")

# command to make a new_character, deleteing the previous character if it exists

    