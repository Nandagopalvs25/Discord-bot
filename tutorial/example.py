from discord.ext import commands
import discord
import asyncio
bot = commands.Bot(command_prefix='!')

@bot.command()  #command example
async def test(ctx):
    await ctx.send('I heard you! {0}'.format(ctx.author.mention))

bot.run('NzQ3Mzg0NTkwMzg5MjE1MzAz.X0OGJA.iZXkYuM73tAZv-MlEvxhcOoDe4o')