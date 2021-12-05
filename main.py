import discord
from discord.ext import commands
import requests
from io import BytesIO

intents = discord.Intents(messages=True)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ConvertToASCII(ctx, content):
    author = ctx.message.author

    r = requests.get('https://thawing-brook-95742.herokuapp.com/braille', params={'url': content, 'get': 'file'})
    
    await ctx.send(file = discord.File(BytesIO(r.content), 'ASCII.txt'))

bot.run('OTE3MDk2NjgwNDcyNTk2NTEw.Yazu1w.XQuPPn0bde01rJo5TO09ZC3CCU8')