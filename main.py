import os

import discord
from discord.ext import commands

import getlive

if __name__ == '__main__':
    DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
    bot = discord.ext.commands.Bot('/sushi ')
    bot.add_cog(getlive.Live(bot))
    bot.run(DISCORD_TOKEN)
