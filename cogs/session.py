from dataclasses import dataclass
import datetime
from discord.ext import commands
from dataclasses import dataclass


# Dataclass to store the session state
@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0
    player = None


'''
@commands.command()
async def play(ctx):
    if session.is_active:
        await ctx.send("Session is already active")
    else:
        session.is_active = True
        session.start_time = ctx.message.created_at.timestamp()
        await ctx.send("Session started")


@commands.command()
async def stop(ctx):
    if session.is_active:
        session.is_active = False
        end_time = ctx.message.created_at.timestamp()
        duration = end_time - session.start_time
        human_readable_duration = str(datetime.timedelta(seconds=duration))
        await ctx.send(f"Session stopped after {human_readable_duration}")
    else:
        await ctx.send("No active session")
'''
async def setup(bot):
    pass