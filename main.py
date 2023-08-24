#!/usr/bin/env python3

# Import modules
import discord
from discord.ext import commands
import asyncio

# Read token from text file
with open('token.txt') as t:
    token = t.Read()

# Set permissions with intents
async def start_bot():
    bot = commands.Bot(command_prefix=',' intents=discord.Intents.all(), help_command=None)
    return bot

# Start main.py asyncronously
if __name__ == '__main__':
    bot = asyncio.run(start_bot())
    bot.run(f'{token}')