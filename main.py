import os
import discord 
from discord.ext import commands

DISCORD_TOKEN = os.environ["discord_token"]
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot.run(f"{DISCORD_TOKEN}")