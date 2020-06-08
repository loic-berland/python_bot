import discord
from discord.ext import commands
import creditentials

secret = creditentials.secret

bot = commands.Bot(command_prefix='!')  # defines which char triggers a command


@bot.event
async def on_ready():
    print('Bot is ready...')

@bot.event
async def on_member_join(member):
    print(f'{member} has join the server')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')

bot.run(secret)
